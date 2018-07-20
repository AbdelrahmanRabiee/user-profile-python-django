from django.forms import ModelForm, inlineformset_factory
from .models import *
from django import forms


class ApplicantModelForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ('candidate', 'created_on', 'updated_on')

        widgets = {
            'birthday': forms.DateInput(attrs={'class': "DOB", 'placeholder': "MM/DD/YYYY"}),
            'birth_place': forms.TextInput(attrs={'placeholder': "place of birth"}),
            'mobile': forms.TextInput(attrs={'placeholder': "966501802558"}),
            'first_name_ar': forms.TextInput(attrs={'placeholder': "first name"}),
            'second_name_ar': forms.TextInput(attrs={'placeholder': "second name"}),
            'third_name_ar': forms.TextInput(attrs={'placeholder': "third name"}),
            'family_name_ar': forms.TextInput(attrs={'placeholder': "family name"}),

        }


class ExperienceModelForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('applicant',)

        widgets = {

            'job_title': forms.TextInput(attrs={'placeholder': "job title"}),
            'employer': forms.TextInput(attrs={'placeholder': "employer"}),
            'start_date': forms.DateInput(attrs={'class': "DOB", 'placeholder': "MM/DD/YYYY"}),
            'end_date': forms.DateInput(attrs={'class': "DOB", 'placeholder': "MM/DD/YYYY"}),

        }


class QualificationModelForm(ModelForm):
    class Meta:
        model = Qualification
        exclude = ('applicant',)

        widgets = {

            'education': forms.TextInput(attrs={'placeholder': "education"}),

        }


ExperienceFormSet = inlineformset_factory(Applicant,Experience,form=ExperienceModelForm,extra=1)
QualificationFormSet = inlineformset_factory(Applicant,Qualification,form=QualificationModelForm,extra=1)



