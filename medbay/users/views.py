from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import User
from .forms import DoctorSignUpForm 


# Create your views here.
# def homeView(request):
#     return render(request,"home.html",{})




class DoctorSignUpView(CreateView):
    model = User 
    form_class = DoctorSignUpForm
    template_name = 'registration/doctor_signup.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return redirect('home')