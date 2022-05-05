from rest_framework import serializers

from library_admin.models import Book
from .models import Author
from library_admin.serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    # book = serializers.StringRelatedField(many=True, read_only=True)
    book = serializers.SlugRelatedField(many=True, read_only=False, slug_field='name', queryset=Book.objects.all())
    # book = BookSerializer(many=True, read_only=False)
    # book = serializers.HyperlinkedRelatedField(view_name='book-detail', many=True, read_only=False)
    class Meta:
        model = Author
        fields = ['name', 'description', 'book']