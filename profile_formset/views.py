from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CreateProfile(LoginRequiredMixin,UpdateView):
    model = Applicant
    template_name = 'create_profile.html'
    fields = ['birthday',
              'birth_place',
              'mobile',
              'first_name_ar',
              'second_name_ar',
              'third_name_ar',
              'family_name_ar',
              'gender','picture','resume']

    success_url = reverse_lazy('profile-list')


    def get_context_data(self, **kwargs):
        data = super(CreateProfile, self).get_context_data(**kwargs)
        if self.request.POST:
            data['experience'] = ExperienceFormSet(self.request.POST,instance=self.object)
            data['qualification'] = QualificationFormSet(self.request.POST,instance=self.object)
        else:
            data['experience'] = ExperienceFormSet(instance=self.object)
            data['qualification'] = QualificationFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        experience = context['experience']
        qualification = context['qualification']
        with transaction.atomic():
            self.object = form.save()

            if experience.is_valid():
                experience.instance = self.object
                experience.save()

            if qualification.is_valid():
                qualification.instance = self.object
                qualification.save()

        return super(CreateProfile, self).form_valid(form)



def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')

        User.objects.create_user(
            username=user_name,
            password=password
        )
        # Applicant.objects.create(
        #     candidate = user_name
        # )
        return redirect('login')
    template_name = 'user_profile/signup.html'
    context = {
        'form': form,

    }

    return render(request, template_name, context)


