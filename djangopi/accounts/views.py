from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = "accounts/signup.html"

    def get_success_url(self):
        return reverse_lazy("login")
