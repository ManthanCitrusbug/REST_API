# from rest_framework.response import Response
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.filters import SearchFilter
# from rest_framework import status
from rest_framework import response, generics, views, viewsets, authentication, permissions, filters, status
from .serializers import BookSerializer, IssuedBookSerialize, UserSerializer, IssuedBookCreateSerializer, AuthorSerializer, UserLoginSerializer
from library_admin.models import Book, Issued_Book
from author.models import Author
from django.contrib.auth.models import User
from .pagination import Mypagination
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend

from api import serializers


class UserCreateListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(views.APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            print('********************')
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            # user = User.objects.filter(username=username)
            # print(user)
            x = authenticate(username=username, password=password)
            if x is not None:
                return response.Response({'msg': "Login Success"}, status = status.HTTP_200_OK)
            else:
                return response.Response({'errors': 'Email or password is incorrect'}, status = status.HTTP_401_UNAUTHORIZED)
        return response.Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


class BookListAPIView(viewsets.ModelViewSet):
    queryset = Book.objects.filter(deleted=False).order_by('id')
    serializer_class = BookSerializer

    pagination_class = Mypagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name', '^category__name', '^author__name']


class IssuedBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookSerialize
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]


class IssuedBookCreateListAPIView(generics.ListCreateAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookCreateSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['email']
    search_fields = ['^book__category__name', '^username', '^email', '^book__name']
    pagination_class = Mypagination


class AuthorListAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.filter(deleted=False).order_by('id')
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name', '^book__name']
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = Mypagination