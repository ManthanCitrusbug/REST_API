from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from library_admin.serializers import BookSerializer, Issued_bookSerialize, UserSerializer
from library_admin.models import Book, Issued_Book
from author.serializers import AuthorSerializer
from author.models import Author
from django.contrib.auth.models import User
from .pagination import Mypagination
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateListAPIView(ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookListAPIView(ModelViewSet):
    queryset = Book.objects.filter(deleted=False).order_by('id')
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = Mypagination


class IssuedBookAPIView(ModelViewSet):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = Issued_bookSerialize
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email']
    pagination_class = Mypagination


class AuthorListAPIView(ModelViewSet):
    queryset = Author.objects.filter(deleted=False).order_by('id')
    serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]