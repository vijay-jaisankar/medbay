from django.contrib import admin
from django.forms.models import ModelForm

from .forms import UserCreationForm,DoctorSignUpForm
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import User,Doctor

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = DoctorSignUpForm
    model = User
    list_display = ("username",)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_superuser', 'is_staff', 'is_active', 'is_doctor','is_patient')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'is_superuser', 'is_staff', 'is_active', 'is_doctor','is_patient')}
            ),
        )



admin.site.register(User, CustomUserAdmin)
admin.site.register(Doctor)