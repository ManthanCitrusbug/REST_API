from asyncio.windows_events import NULL
from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers
from author.models import Author
from library_admin.models import Book, Issued_Book, Category
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from library_admin.tasks import send_mail_task
from django.db.models import Q
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # company = serializers.StringRelatedField(read_only=True)
    # company = CompanySerializer(many=True)
    company = serializers.SlugRelatedField(read_only=True, slug_field='name')
    token = serializers.SerializerMethodField('get_token_key')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
            'email', 'token', 'password', 'company']
        extra_kwargs = {'password': {'write_only': True}}

    def get_token_key(self, obj):
        token = Token.objects.get_or_create(user_id=obj.id)[0].key
        return token

    def create(self, validated_data):
        user = super().create(validated_data)
        # x = str(user.email)
        # if x.find('gmail') or x.find('yopmail'):
        #     user.company = None
        # else:
        #     query = User.objects.all()
        #     ids = []
        #     for i in query:
        #         ids.append(i)
        #     if user.id == min(ids):
        #         user.company = None
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    @receiver(post_save, sender=User)
    def create_token(sender, instance, created, **kwargs):
        if created:
            Token.objects.create(user=instance)
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if not email:
            raise serializers.ValidationError("Enter the email.")
        if not password:
            raise serializers.ValidationError("Enter the password.") 
        return data


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=True, read_only=False, slug_field='name', queryset=Author.objects.all())
    category = serializers.SlugRelatedField(read_only=False, slug_field='name', queryset=Category.objects.all())
    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category', 'author']


class IssuedBookSerialize(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Issued_Book
        fields = '__all__'

    def validate(self, data):
        issued_date = data.get('issued_date')
        re_book = data.get('return_date')

        days = NULL
        if re_book != None:
            days = re_book - issued_date
            if days.days < 0:
                raise serializers.ValidationError("Enter valid return date.")
        return data

    def save(self, **kwargs):
        user = super().save(**kwargs)
        qun = Book.objects.get(name=user.book)
        x = qun.quantity + 1
        Book.objects.filter(name=user.book).update(quantity=x)
        user.save()
        if user.return_date is not None:
            # send_mail_task.delay(user.email, user.return_date)
            send_mail_task.delay(user.id)
        return user

class IssuedBookCreateSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(read_only=False, slug_field='name', queryset=Book.objects.all())
    class Meta:
        model = Issued_Book
        fields = "__all__"

    def validate(self, data):
        issued_date = data.get('issued_date')
        email_data = data.get('email')
        book_name = data.get('book')

        if Issued_Book.objects.filter(email=email_data, book__name=book_name, return_date=None).exists():
            raise serializers.ValidationError("User has already issued this book.")

        if issued_date < date.today():
            raise serializers.ValidationError("Enter valid issue date.")

        book_instance = Book.objects.get(name=book_name, deleted=False)
        if book_instance.quantity == 0:
            raise serializers.ValidationError("Book is not available.")

        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        qun = Book.objects.get(name=user.book)

        if qun.quantity>0:
            x = qun.quantity - 1
            Book.objects.filter(name=user.book).update(quantity=x)
            user.save()
        return user


class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(many=True, read_only=False, slug_field='name', queryset=Book.objects.all())
    class Meta:
        model = Author
        fields = ['name', 'description', 'book']