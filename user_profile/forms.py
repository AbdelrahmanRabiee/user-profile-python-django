from .models import *
from django import forms
from betterforms.multiform import MultiModelForm


class ApplicantModelForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ('candidate','created_on','updated_on')

        widgets = {
            'birthday':forms.DateInput(attrs={'id':"DOB",'placeholder':"MM/DD/YYYY"}),
            'birth_place': forms.TextInput(attrs={'placeholder':"place of birth"}),
            'mobile': forms.TextInput(attrs={'placeholder': "966501802558"}),
            'first_name_ar': forms.TextInput(attrs={'placeholder': "first name"}),
            'second_name_ar': forms.TextInput(attrs={'placeholder': "second name"}),
            'third_name_ar': forms.TextInput(attrs={'placeholder': "third name"}),
            'family_name_ar': forms.TextInput(attrs={'placeholder': "family name"}),


        }

class ExperienceModelForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ('applicant',)
        widgets = {


            'job_title': forms.TextInput(attrs={'placeholder': "job title"}),
            'employer': forms.TextInput(attrs={'placeholder': "employer"}),
            'start_date': forms.DateInput(attrs={'id': "startDate", 'placeholder': "MM/DD/YYYY"}),
            'end_date': forms.DateInput(attrs={'id': "endDate", 'placeholder': "MM/DD/YYYY"}),

        }

class QualificationModelForm(forms.ModelForm):
    class Meta:
        model = Qualification
        exclude = ('applicant',)

        widgets = {

            'education': forms.TextInput(attrs={'placeholder': "education"}),

        }



class ProfileMultiModelForm(MultiModelForm):
    form_classes = {
        'applicant':ApplicantModelForm,
        'experience':ExperienceModelForm,
        'qualification':QualificationModelForm

    }


