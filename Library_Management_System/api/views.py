from email import header
from importlib.resources import Resource
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer, IssuedBookSerialize, UserSerializer, IssuedBookCreateSerializer, AuthorSerializer
from library_admin.models import Book, Issued_Book
from author.models import Author
from django.contrib.auth.models import User
from .pagination import Mypagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookListAPIView(ModelViewSet):
    queryset = Book.objects.filter(deleted=False).order_by('id')
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = Mypagination
    filter_backends = [SearchFilter]
    search_fields = ['^name', '^category__name', '^author__name']


class IssuedBookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookSerialize
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['email']
    search_fields = ['^category__name', '^username', '^email', '^book__name']
    pagination_class = Mypagination


class IssuedBookCreateListAPIView(ListCreateAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['^category__name', '^username', '^email', '^book__name']
    pagination_class = Mypagination


class AuthorListAPIView(ModelViewSet):
    queryset = Author.objects.filter(deleted=False).order_by('id')
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name', '^book__name']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]