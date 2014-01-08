from django.contrib import admin
from django.contrib.auth.admin import User, UserAdmin

from forum.models import Thread, Forum, Reply
from forum.forms import ForumUserChangeForm, ForumUserCreationForm


class ForumUserAdmin(UserAdmin):
    form = ForumUserChangeForm
    add_form = ForumUserCreationForm


class ForumAdmin (admin.ModelAdmin):
    list_display = ('name',)


class ThreadAdmin (admin.ModelAdmin):
    list_display = ('title',)


class ReplyAdmin (admin.ModelAdmin):
    list_display = ('parent', 'user', 'content')


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Reply, ReplyAdmin)

