from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'author'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add-author', views.AddAuthorView.as_view(), name='add-author'),
    path('author-list', views.AuthorListView.as_view(), name='author-list'),
    path('author-details/<int:pk>', views.AuthorDetailView.as_view(), name='author-details'),
    path('author-edit/<int:pk>', views.EditAuthorView.as_view(), name='author-edit'),
    path('author-delete/<int:pk>', views.DeleteAuthorView.as_view(), name='author-delete'),
]