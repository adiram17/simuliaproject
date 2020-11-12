from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.home, name='home'),
    path('serelia_list', views.sereliaList, name='serelia_list'),
    path('serelia_create', views.sereliaCreate, name='serelia_create'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('change_password', views.changePassword, name='change_password'),
]
