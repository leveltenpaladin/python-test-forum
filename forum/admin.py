from django.contrib import admin
from forum.models import ForumUser, Thread, Forum, Reply

# Register your models here.


class ForumUserAdmin(admin.ModelAdmin):
    pass


class ForumAdmin (admin.ModelAdmin):
    list_display = ('name',)


class ThreadAdmin (admin.ModelAdmin):
    list_display = ('title',)


class ReplyAdmin (admin.ModelAdmin):
    list_display = ('parent', 'user', 'content')


admin.site.register(ForumUser, ForumUserAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Reply, ReplyAdmin)

