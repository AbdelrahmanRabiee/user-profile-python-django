from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify
import random
import os
import datetime

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_location_picture(instance,filename):
    new_filename = random.randint(1,21452541)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "user/{final_filename}".format(final_filename=final_filename)





def upload_location_resume(instance,filename):
    new_filename = random.randint(1,21452541)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "resume/{final_filename}".format(final_filename=final_filename)



def upload_location_experience_letter(instance,filename):
    new_filename = random.randint(1,21452541)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "resume/{final_filename}".format(final_filename=final_filename)



class Applicant(models.Model):
    candidate = models.OneToOneField(User, on_delete=models.SET_NULL, verbose_name=_('Government ID'), blank=False,
                                null=True,
                                related_name='user_applicant',
                                validators=[
                                    RegexValidator(
                                        '^(1)\d{9}$',
                                        message=_("You have entered an invalid Government ID")
                                    ), ])
    birthday = models.DateField(_('Birthday'), null=True, blank=True)
    birth_place = models.CharField(_('Birth Place'),
                                   null=True,
                                   blank=True,
                                   max_length=100,
                                   help_text=_('Country and city. e.g. Saudi Arabia Jeddah'))
    mobile = models.CharField(
        _('Mobile'),
        null=True,
        blank=False,
        max_length=12,
        help_text=_(
            'Mobile number should be of this format "9665xxxxxxxx". <br>Use English numerals only. <br>Please make sure to activate promotional messages from your mobile provider.'),
        validators=[
            RegexValidator(
                '^(9665|٩٦٦٥)\d{8}$',
                message=_('You have entered an invalid mobile number')
            ),
        ],
    )
    first_name_ar = models.CharField(null=True, blank=True, max_length=50, verbose_name=_('First Name (Arabic)'))
    second_name_ar = models.CharField(null=True, blank=True, max_length=50, verbose_name=_('Second Name (Arabic)'))
    third_name_ar = models.CharField(null=True, blank=True, max_length=50, verbose_name=_('Third Name (Arabic)'))
    family_name_ar = models.CharField(null=True, blank=True, max_length=50, verbose_name=_('Family Name (Arabic)'))
    GENDER_CHOICES = (
        ('', _("---")),
        ('M', _('Male')),
        ('F', _('Female'))
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, default='', verbose_name=_('Gender'))
    picture = models.FileField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name=_('Personal Picture'),
        upload_to=upload_location_picture,
        #validators=[validate_image_extension],
        #help_text=_('Allowed formats: jpg, png, bmp, gif.')
    )
    resume = models.FileField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name=_('upload your resume'),
        upload_to=upload_location_resume,
        # validators=[validate_image_extension],
        # help_text=_('Allowed formats: jpg, png, bmp, gif.')
    )
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True, )
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True, )

    def __str__(self):
        return str(self.candidate)

    # @receiver(post_save, sender=User)
    # def create_user_candidate(sender, instance, created, **kwargs):
    #     if created:
    #         Applicant.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_candidate(sender, instance, **kwargs):
    #     try:
    #         instance.applicant.save()
    #     except:
    #         applicant = Applicant.objects.create(user=instance)
    #
    # def get_applicant_full_name(self):
    #     if self.first_name_ar and self.second_name_ar and self.third_name_ar and self.family_name_ar:
    #         return '%s %s %s %s' % (self.first_name_ar, self.second_name_ar, self.third_name_ar, self.family_name_ar)


class Experience(models.Model):
    applicant = models.ForeignKey(Applicant, models.SET_NULL, blank=False, null=True,
                                  )
    job_title = models.CharField(_('Job title'), max_length=250, null=True, blank=False)
    employer = models.CharField(_('Employer'), max_length=250, null=True, blank=False)
    start_date = models.DateField(_('Start date'), null=True, blank=False)
    end_date = models.DateField(_('End date'), null=True, blank=True)
    experience = models.FileField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name=_('Experience letter'),
        upload_to=upload_location_experience_letter,
        # validators=[validate_image_extension],
        # help_text=_('Allowed formats: jpg, png, bmp, gif.')
    )

    def __str__(self):
        return self.job_title


class Qualification(models.Model):
    applicant = models.ForeignKey(Applicant, models.SET_NULL, null=True)
    TYPES = (
        ('Elementary school', _('Elementary school')),
        ('Intermediate school', _('Intermediate school')),
        ('High school', _('High school')),
        ('Diploma', _('Diploma')),
    )
    type = models.CharField(_('Type'), max_length=250, null=True, blank=False, choices=TYPES)
    education = models.CharField(_('Education'), max_length=250, null=True, blank=False)


    def __str__(self):
        return self.education
