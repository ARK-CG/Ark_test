from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def index(request):
    return render(request, 'ark_account/index.html')


def logout(request):
    return render(request, 'ark_account/index.html')


def signup(request):
    return render(request, 'ark_account/index.html')

class TopPageView(generic.TemplateView):
    template_name = "ark_account/index.html"
 
 
class MyPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "ark_account/info.html"
 
 
class CreateUserView(generic.CreateView):
    template_name = 'ark_account/create.html'
    form_class = RegisterForm
    success_url = reverse_lazy('ark_account:index')

def authlogin(request,user_name,user_password):
    user = authenticate(request,username=user_name,password=user_password)
    if user is not None:
        login(request,user)
        return redirect('/account/')
    else:
        return redirect('/account/login')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_password = request.POST['password']
        if 'sign_btn' in request.POST:
            user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            ) 
            user.save()
            return authlogin(request,user_name,user_password)
        if 'login_btn' in request.POST:
            return authlogin(request,user_name,user_password)
    return render(request,'ark_account/login.html')