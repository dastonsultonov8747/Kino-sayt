from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('signup/', views.signup_view, name='signup'),  # Ro'yxatdan o'tish uchun URL
    path('login/', views.login_view, name='login'),  # Login uchun URL
    path('logout/', views.logout_view, name='logout'),  # Logout uchun URL
]
