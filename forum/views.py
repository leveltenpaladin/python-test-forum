from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import FormView

from forum.models import Forum, Thread

def landing_redirect(request):
    return redirect('/forum/')


class LandingView(TemplateView):
    template_name = 'forum/index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['forums'] = Forum.get_root_forums()
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
    template_name = 'forum/signup.html'
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


class ForumDetailView(DetailView):
    model = Forum
    context_object_name = 'forum'



