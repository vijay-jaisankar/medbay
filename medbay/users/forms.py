from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Doctor,Patient,User


class DoctorSignUpForm(UserCreationForm):
    registrationNumber = forms.IntegerField(required=True)

    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields #+ ('registrationNumber',) 

    @transaction.atomic
    def save(self):
        userBase = super().save(commit=False)
        userBase.is_doctor = True
        userBase.save()
        doctor = Doctor.objects.create(user=userBase)
        doctor.registrationNumber = self.cleaned_data['registrationNumber']
        doctor.save()
        return userBase