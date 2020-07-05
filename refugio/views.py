from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext, ugettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import auth
# Create your views here.
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm)
User = get_user_model()


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('home')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'registration/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name = 'registration/password_reset_confirm.html'
	form_class = SetPasswordForm
	success_url = reverse_lazy('password_reset_complete')
	form_valid_message = _("Your password was changed!")
	

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
    success_url = reverse_lazy('login')