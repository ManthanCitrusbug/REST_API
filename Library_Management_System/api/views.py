from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
# from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.db.models import Q
from .serializers import BookSerializer, IssuedBookSerialize, UserSerializer, IssuedBookCreateSerializer, AuthorSerializer, UserLoginSerializer, AddCompanySerializer
from library_admin.models import Book, Issued_Book
from author.models import Author
from django.contrib.auth.models import User
from .pagination import Mypagination
from .models import Company
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddCompanyAPIView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = AddCompanySerializer
    # # response_serializerr = AddCompanySerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Company.objects.filter(Q(name=serializer.validated_data.get('name'))).count() == 0:
            self.perform_create(serializer)
            
        else:
            self.perform_create(serializer)
            x = Company.objects.filter(name=serializer.validated_data.get('name')).last()
            x.role = Company.USER
            x.save()
            serializer = self.serializer_class(x)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(APIView): 
    def post(self, request, format=None):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            email = serializers.data.get('email')
            password = serializers.data.get('password')
            x = User.objects.get(email=email)
            user = authenticate(username=x.username, password=password)
            if user is not None:
                get_token = Token.objects.get(user=user)
                return Response({'token': get_token.key}, status = status.HTTP_200_OK)
            else:
                return Response({'error': 'invalid details'}, status = status.HTTP_404_NOT_FOUND)
        return Response(serializers.data, status = status.HTTP_400_BAD_REQUEST)


class BookListAPIView(ModelViewSet):
    queryset = Book.objects.filter(deleted=False).order_by('id')
    serializer_class = BookSerializer
    pagination_class = Mypagination
    filter_backends = [SearchFilter]
    search_fields = ['^name', '^category__name', '^author__name']


class IssuedBookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookSerialize
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class IssuedBookCreateListAPIView(ListCreateAPIView):
    queryset = Issued_Book.objects.all().order_by('id')
    serializer_class = IssuedBookCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['email']
    search_fields = ['^book__category__name', '^username', '^email', '^book__name']
    pagination_class = Mypagination


class AuthorListAPIView(ModelViewSet):
    queryset = Author.objects.filter(deleted=False).order_by('id')
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name', '^book__name']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = Mypagination