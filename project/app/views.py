from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm, LoginForm, User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')



def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
           user_form.save()
        return HttpResponse("<h1>Registration successfully</h1>")

    else:
        user_form=RegistrationForm()
        return render(request, 'registration.html',{'user_form':user_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse("<h1> Disable account </h1> ")
            else:
                return HttpResponse("<h1> Invalid Login </h1> ")

    else:
        form= LoginForm()

    return render(request, "login.html" ,{"form": form})
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

def detail(request):
    all = User.objects.all()
    return render(request, 'detail.html',{"all":all})

def update(request, id):
    if request.method == 'POST':
        b = User.objects.get(pk= id)
        fm = RegistrationForm(request.POST, instance=b)
        if fm.is_valid():
            fm.save()
    else:
        b = User.objects.get(pk=id)
        fm = RegistrationForm( instance=b)
    return render(request,'update.html',{'form':fm})


def delete(request,id):
    if request.method == "POST":
        dl = User.objects.get(pk = id)
        dl.delete()
        return HttpResponseRedirect('/')

