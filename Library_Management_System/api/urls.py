from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from api import views
# from library_admin import APIviews
# from author import APIviews as authorview

router = DefaultRouter()

router.register('book-api', views.BookListAPIView, basename='book-api')
router.register('issued-book-api', views.IssuedBookAPIView, basename='issued-book-api')
router.register('author-api', views.AuthorListAPIView, basename='author-api')
# router.register('create-list-user', views.UserCreateListAPIView, basename='author-api')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('create-list-user/', views.UserCreateListAPIView.as_view(), name='create-list-user'),
    # path('issued-book-list-create-user/', views.IssuedBookListAPIView.as_view(), name='issued-book-list-create-user'),
    # path('auth/', include('rest_framework.urls')),
]
