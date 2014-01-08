from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from models import Forum


class ForumCreationForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['parent', 'name']

    def save(self, commit=True):
        forum = super(ForumCreationForm, self).save(commit=False)
        forum.creator = self.user
        if commit:
            forum.save()
        return forum



class ForumUserCreationForm(UserCreationForm):
    pass


class ForumUserChangeForm(UserChangeForm):
    pass


