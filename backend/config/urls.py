"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (LoginView, LogoutView,
    PasswordResetView,
    PasswordResetForm, 
    PasswordResetDoneView,
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeForm,
    PasswordChangeDoneView,
    
     )

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/Form/', PasswordResetForm, name='password_reset_Form'),
    path('accounts/password/done/', PasswordChangeView.as_view(), name='password_reset_done'),
    path('accounts/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/change/', PasswordChangeForm, name='password_reset_change'),
    path('accounts/password/reset/confirm/', PasswordChangeDoneView.as_view(), name='password_reset_change_done'),
    path('accounts/password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
    path('accounts/', include('accounts.urls')),
]
