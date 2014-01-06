from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext, loader, Context
from django.http import HttpResponse

from forum.models import Forum, Thread


def landing_redirect(request):
    return redirect("/forum/")


def landing(request):
    forums = Forum.objects.filter(parent=None)
    threads = {}
    sub_forums = {}
    for forum in forums:
        sub_forums[forum.id] = Forum.objects.filter(parent=forum)
        threads[forum.id] = Thread.objects.filter(parent_forum=forum)

    context = RequestContext(request, {
        'forums': forums,
        'sub_forums': sub_forums
    })
    template = loader.get_template('forum/index.html')

    return HttpResponse(template.render(context))


def user_login(request):
    if ('username' in request.POST) & ('password' in request.POST):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)

    return redirect("/forum/")


def user_logout(request):
    logout(request)
    return redirect("/forum/")


def signup(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/forum/")
    else:
        user_form = UserCreationForm()

    context = RequestContext(request, {
        'form': user_form,
    })
    template = loader.get_template('forum/signup.html')
    return HttpResponse(template.render(context))


def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    context = RequestContext(request, {
        'forum': forum,
    })
    template = loader.get_template('forum/forum_detail.html')
    return HttpResponse(template.render(context))


def thread_detail(request, forum_id,  thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    context = RequestContext(request, {
        'thread': thread,
    })
    template = loader.get_template('forum/thread_detail.html')
    return HttpResponse(template.render(context))


