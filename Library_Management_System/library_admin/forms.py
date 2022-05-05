from datetime import date
from asyncio.windows_events import NULL
from django import forms
from django.contrib.auth.models import User
from author.models import Author
from library_admin.models import Book, Issued_Book

class AdminRegisterform(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control w-50 m-auto'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),             
            'first_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),             
            'last_name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),             
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),    
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'password' : forms.PasswordInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }


class AddBookForm(forms.ModelForm):

    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.SelectMultiple(attrs={'class' : 'form-control w-50 m-auto'}), required=False)

    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category']
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'description' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'quantity' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'category' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }

    def save(self, commit=True):
        user = super(AddBookForm, self).save(commit=False)
        data = self.cleaned_data
        if commit:
            user.save()
            x = Book.objects.get(name=user.name, deleted=False)
            author_name = data['author']
            for i in author_name:
                author = Author.objects.get(name=i)
                author.book.add(x)
        return user


class EditBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'description', 'quantity', 'category']
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'description' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'quantity' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'category' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }


class Issue_Book_Form(forms.ModelForm):
    class Meta:
        model = Issued_Book
        fields = ['username', 'email', 'address', 'book', 'issued_date', 'return_date', 'charge_per_day']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'address' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'book' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),        
            'issued_date' : forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'charge_per_day' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }

    def clean(self):
        data = super(Issue_Book_Form, self).clean()
        book_name = data.get('book')
        email_data = data.get('email')
        issued_date = data.get('issued_date')
        if Issued_Book.objects.filter(email=email_data, book__name=book_name, return_date=None).exists():
             raise forms.ValidationError("User has already issued this book.")
        if issued_date < date.today():
            raise forms.ValidationError("Enter valid date.")
        if book_name:
            book_instance = Book.objects.get(name=book_name, deleted=False)
            if book_instance.quantity == 0:
                raise forms.ValidationError("Book is not available.")
        return super().clean()
    
    def save(self, commit=True):
        user = super().save(commit=False)
        qun = Book.objects.get(name=user.book)
        if commit:
            if qun.quantity>0:
                x = qun.quantity - 1
                Book.objects.filter(name=user.book).update(quantity=x)
                user.save()
        return user


class Issue_Book_Edit_Form(forms.ModelForm):
    class Meta:
        model = Issued_Book
        fields = ['username', 'email', 'address', 'book', 'issued_date', 'return_date', 'charge_per_day']
        widgets = {
            'username' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'email' : forms.EmailInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'address' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'book' : forms.Select(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),        
            'issued_date' : forms.DateInput(
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'return_date' : forms.DateInput(
                attrs={'class' : 'form-control w-50 m-auto',
                'type' : 'date'}
            ),
            'charge_per_day' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }

    def clean(self):
        cleaned_data = super(Issue_Book_Edit_Form, self).clean()
        date = cleaned_data.get('issued_date')
        re_book = cleaned_data.get("return_date")
        days = NULL
        if re_book != None:
            days = re_book - date
            if days.days < 0:
                raise forms.ValidationError("Enter valid return date.")
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        qun = Book.objects.get(name=user.book)
        if commit:
            if user.return_date != None:
                x = qun.quantity + 1
                Book.objects.filter(name=user.book).update(quantity=x)
            else:
                pass
            user.save()
        return user