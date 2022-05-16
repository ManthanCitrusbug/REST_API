import imp
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('book-api', APIviews.BookListAPIView, basename='book-api')
# router.register('issued-book-api', APIviews.IssuedBookAPIView, basename='issued-book-api')

app_name = 'library_admin'



urlpatterns = [
    # path('celery', views.CeleryTaskView.as_view(), name='celery'),
    # path('admin/', admin.site.urls),
    path('index', views.IntexView.as_view(), name='index'),
    path('admin-register', views.AdminRegisterView.as_view(), name='admin-register'),
    path('admin-login', views.AdminLoginView.as_view(), name='admin-login'),
    path('admin-logout', views.AdminLogoutView.as_view(), name='admin-logout'),
    path('admin-dashboard', views.AdminDashboardView.as_view(), name='admin-dashboard'),
    path('add-book', views.AddBookView.as_view(), name='add-book'),
    path('edit-book/<int:pk>', views.EditBookView.as_view(), name='edit-book'),
    path('detail-book/<int:pk>', views.BookDetailView.as_view(), name='detail-book'),
    path('delete-book/<int:pk>', views.DeleteBookView.as_view(), name='delete-book'),
    path('issue-book', views.IssueBookView.as_view(), name='issue-book'),
    path('issued-books-list', views.IssuedBooksListView.as_view(), name='issued-books-list'),
    path('issued-books-details/<int:pk>', views.IssuedBookDetailsView.as_view(), name='issued-books-details'),
    path('issued-books-edit/<int:pk>', views.IssuedBookEditView.as_view(), name='issued-books-edit'),
    path('issued-books-delete/<int:pk>', views.IssuedBookDeleteView.as_view(), name='issued-books-delete'),
]