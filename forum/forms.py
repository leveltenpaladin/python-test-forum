from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from forum import models


class UserSignupForm(ModelForm):
    class Meta:
        model = User
        fields = {'username', 'password'}
