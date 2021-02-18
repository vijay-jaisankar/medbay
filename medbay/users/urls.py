from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView

from .views import DoctorSignUpView #,PatientSignUpView

urlpatterns = [
    path('signup/doctor/',DoctorSignUpView.as_view(),name='doctor_signup'),
    # path('home/',homeView,name='home'),
    path('login/doctor/', LoginView.as_view(template_name="registration/doctor_login.html"), name='doctor_login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # path('signup/patient/',PatientSignUpView.as_view(),name='patient signup'),
]