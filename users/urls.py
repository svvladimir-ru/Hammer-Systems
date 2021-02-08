from django.urls import path, include
from . import views


urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('login_telefon/', views.login_telefon, name='login_telefon'),
    path('<user>/<int:code_email>', views.login2, name='login2'),
    path('<user>/', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout')
]

