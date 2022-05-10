from django.urls import path
from . import views

app_name = 'customadmin'

urlpatterns = [
    path('dashboard', views.IndexView.as_view(), name='dashboard'),
    path('user-create', views.UserCreateView.as_view(), name='user-create'),
    path('user-login', views.UserLoginView.as_view(), name='user-login'),
    path('user-list-ajax', views.UserAjaxPagination.as_view(), name='user-list-ajax'),
    path('user-details', views.UserDetailView.as_view(), name='user-details'),
    path('user-delete', views.UserDeleteView.as_view(), name='user-delete'),
    path('user-list', views.UserListView.as_view(), name='user-list'),
]