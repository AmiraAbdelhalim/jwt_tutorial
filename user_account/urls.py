from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.contrib.auth import views as django_auth_views

app_name = 'user_account'
urlpatterns = [

    path('hello/', hello_world, name='hello_world'),
    path('test/', test, name='test'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login/', django_auth_views.LoginView.as_view(), name='login'),
    path('logout/', django_auth_views.LogoutView.as_view(), name='logout'),
]