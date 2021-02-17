from django.urls import path


from .views import DoctorSignUpView,homeView #,PatientSignUpView

urlpatterns = [
    path('signup/doctor/',DoctorSignUpView.as_view(),name='doctor signup'),
    path('home/',homeView,name='home'),
    # path('signup/patient/',PatientSignUpView.as_view(),name='patient signup'),
]