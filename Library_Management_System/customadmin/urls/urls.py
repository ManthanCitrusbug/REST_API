from django.urls import path
from . import views

app_name = 'customadmin'

urlpatterns = [
    path('dashboard', views.IndexView.as_view(), name='dashboard'),
    path('user/create', views.UserCreateView.as_view(), name='user-create'),
    path('user/login', views.UserLoginView.as_view(), name='user-login'),
    path('user/list-ajax', views.UserAjaxPagination.as_view(), name='user-list-ajax'),
    path('user/details/<int:pk>', views.UserDetailView.as_view(), name='user-details'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(), name='user-delete'),
    path('user/update/<int:pk>', views.UserUpdateView.as_view(), name='user-update'),
    path('user/list', views.UserListView.as_view(), name='user-list'),
    # Book
    path('book/list', views.BookListView.as_view(), name='book-list'),
    path('book/create', views.BookCreateView.as_view(), name='book-create'),
    path('book/details/<int:pk>', views.BookDetailsView.as_view(), name='book-details'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name='book-delete'),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(), name='book-update'),
    path('book/list-ajax', views.BookAjaxPagination.as_view(), name='book-list-ajax'),
    # Author
    path('author/list', views.AuthorListView.as_view(), name='author-list'),
    path('author/create', views.AuthorCreateView.as_view(), name='author-create'),
    path('author/details/<int:pk>', views.AuthorDetailsView.as_view(), name='author-details'),
    path('author/delete/<int:pk>', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('author/update/<int:pk>', views.AuthorUpdateView.as_view(), name='author-update'),
    path('author/list-ajax', views.AuthorAjaxPagination.as_view(), name='author-list-ajax'),
]