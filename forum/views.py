from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template import RequestContext, loader, Context
from django.http import HttpResponse
from django.shortcuts import render

from forum.models import Forum, Thread


def landing_redirect(request):
    return redirect('/forum/')


def landing(request):
    return render(request, 'forum/index.html', RequestContext(request, {
        'forums': Forum.get_root_forums(),
    }))


def user_login(request):
    form = AuthenticationForm(request.POST)
    if form.is_valid():
        form.clean()
        if form.get_user() is not None:
            login(request, form.get_user())

    return redirect('/forum/')


def user_logout(request):
    logout(request)
    return redirect('/forum/')


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/forum/')
    else:
        user_form = UserCreationForm()

    return render(request, 'forum/signup.html', RequestContext(request, {
        'form': user_form,
    }))


def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    return render(request, 'forum/forum_detail.html', RequestContext(request, {
        'forum': forum,
    }))



def thread_detail(request, forum_id,  thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'forum/thread_detail.html', RequestContext(request, {
        'thread': thread,
    }))



