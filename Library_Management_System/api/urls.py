from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from api import views

router = DefaultRouter()

router.register('book', views.BookListAPIView, basename='book')
router.register('author', views.AuthorListAPIView, basename='author')
router.register('company', views.AddCompanyAPIView, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    # path('user/create/', views.UserCreateListAPIView.as_view(), name='user/create/'),
    path('user/list/', views.UserCreateListAPIView.as_view(), name='user/list/'),
    # path('company/list/', views.AddCompanyAPIView.as_view(), name='company/list/'),
    path('user/login/', views.UserLoginAPIView.as_view(), name='user/login/'),
    # path('issued-book/create/', views.IssuedBookCreateListAPIView.as_view(), name='issued-book-create'),
    path('issued-book/list/', views.IssuedBookCreateListAPIView.as_view(), name='issued-book-list'),
    path('issued-book/update/<int:pk>', views.IssuedBookAPIView.as_view(), name='issued-book-update'),
]
