from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import *
from django.views.generic import ListView,CreateView,TemplateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from profile_formset.models import Applicant
from django.contrib.auth import login as auth_login
# Create your views here.
class Home(TemplateView):
    template_name = 'user_profile/home.html'


class ProfileCreateView(CreateView):
    form_class = ProfileMultiModelForm
    success_url = reverse_lazy('profile-list')
    template_name = 'user_profile/create_profile.html'

    def get_queryset(self):
        queryset = super(ProfileCreateView,self).get_queryset()
        return queryset.filter(user__email=self.request.email)

    def form_valid(self, form):
        applicant = form['applicant'].save(commit=False)
        applicant.candidate = self.request.user
        applicant.save()
        experience = form['experience'].save(commit=False)
        experience.applicant = applicant
        experience.save()
        qualification = form['qualification'].save(commit=False)
        qualification.applicant = applicant
        qualification.save()

        return redirect('home')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'user_profile/signup.html'


    def form_valid(self, form):
        username = form.cleaned_data['username']
        form.save()
        user = User.objects.get(username=username)
        Applicant.objects.create(
            candidate = user
        )
        return super(SignUp, self).form_valid(form)

class SignIn(FormView):

    # success_url = reverse_lazy('profile-formset-add',kwargs={'pk': instance.pk})
    form_class = AuthenticationForm
    template_name = 'user_profile/signin.html'


    def form_valid(self, form):
        pk = form.get_user()
        auth_login(self.request, form.get_user())
        return super(SignIn, self).form_valid(form)

    def get_success_url(self):
        pk = Applicant.objects.get(candidate=self.request.user).pk
        return reverse_lazy('profile-formset-add',kwargs={'pk': pk})