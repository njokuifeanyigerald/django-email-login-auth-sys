from django.urls import path

from .views import LoginView, RegisterView,home,logoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="homr"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
