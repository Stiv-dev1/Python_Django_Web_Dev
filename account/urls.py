from django.urls import path, include
from account import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView,\
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.base, name='base'),
    path('changepasswd', views.changepasswd, name='changepasswd'),
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(), name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('profile', views.profile, name='profile'),
    path('profile-update', views.profile_update, name='profile-update'),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]