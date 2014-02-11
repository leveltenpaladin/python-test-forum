from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import FormView

from forum.models import Forum, Thread
from forum.forms import ForumCreationForm, ThreadCreationForm

import logging

logger = logging.getLogger(__name__)


def landing_redirect(request):
    return redirect('/forum/')


class LandingView(TemplateView):
    template_name = 'forum/index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['forums'] = Forum.get_root_forums()
        return context


class ThreadCreationView(CreateView):
    template_name = 'forum/create_thread.html'
    form_class = ThreadCreationForm
    success_url = '/forum/'

    def form_valid(self, form):
        form.instance.op = self.request.user
        return super(ThreadCreationView, self).form_valid(form)

    def get_initial(self):
        parent = get_object_or_404(Forum, id=self.kwargs['pk'])
        return {
            'parent_forum': parent,
        }

    def get_context_data(self, **kwargs):
        context = super(ThreadCreationView, self).get_context_data(**kwargs)
        parent_id = self.kwargs['pk']
        if parent_id is None:
            parent_id = 0
        context['parent_forum_id'] = parent_id
        return context


class ForumCreationView(CreateView):
    template_name = 'forum/create_forum.html'
    form_class = ForumCreationForm
    success_url = '/forum/'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(ForumCreationView, self).form_valid(form)

    def get_initial(self):
        parent = get_object_or_404(Forum, id=self.kwargs['pk'])
        return {
            'parent': parent,
        }

    def get_context_data(self, **kwargs):
        context = super(ForumCreationView, self).get_context_data(**kwargs)
        parent_id = self.kwargs['pk']
        if parent_id is None:
            parent_id = 0
        context['parent_id'] = parent_id
        return context


class SignUpView(FormView):
    template_name = 'forum/signup.html'
    form_class = UserCreationForm
    success_url = '/forum/'

    def form_valid(self, form):
        username = form.clean_username()
        password = form.clean_password2()
        form.save()
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(SignUpView, self).form_valid(form)


class LogInView(FormView):
    template_name = 'forum/login.html'
    form_class = AuthenticationForm
    success_url = '/forum/'

    def form_valid(self, form):
        form.clean()
        if form.get_user() is not None:
            login(self.request, form.get_user())
        return super(LogInView, self).form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/forum/')


class ThreadDetailView(DetailView):
    model = Thread
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super(ThreadDetailView, self).get_context_data(**kwargs)
        context['parent'] = self.object.parent_forum
        context['replies'] = self.object.get_replies
        return context


class ForumDetailView(DetailView):
    model = Forum
    context_object_name = 'forum'

    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)
        context['parent'] = self.object.parent
        context['threads'] = self.object.get_threads()
        context['children'] = self.object.get_sub_forums()
        return context



