from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, Select, Textarea

from models import Forum, Thread, Reply


class ForumCreationForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['parent', 'name']
        widgets = {
            'parent': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class ThreadCreationForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['parent_forum', 'title']
        widgets = {
            'parent_forum': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
        }


class ReplyCreationForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['parent', 'content']
        widgets = {
            'parent': Select(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
        }


class ForumUserCreationForm(UserCreationForm):
    pass


class ForumUserChangeForm(UserChangeForm):
    pass


