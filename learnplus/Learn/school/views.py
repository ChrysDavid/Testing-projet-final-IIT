from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_request, logout
from django.shortcuts import render , redirect 
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 
from django.contrib import messages


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student_user'):
            return redirect('index_student')
        elif hasattr(request.user, 'instructor'):
            return redirect('dashboard')
        else:
            return redirect('/admin/')  # Par défaut
    return render(request, 'pages/guest-login.html', {})




def signup(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except:
            print("3")
            return redirect("/admin/")
    else:

        datas = {

        }
        return render(request, 'pages/guest-signup.html', datas) 

def forgot_password(request):
    if request.user.is_authenticated:
        try:
            try:
                print("1")
                if request.user.student_user:
                    return redirect('index_student')
            except:
                print("2")
                if request.user.instructor:
                    return redirect('dashboard')
        except:
            print("3")
            return redirect("/admin/")
    else:
        datas = {

        }
        return render(request, 'pages/guest-forgot-password.html', datas)



def islogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login_request(request, user)
            try:
                if hasattr(user, 'student_user'):
                    return redirect('index_student')
                elif hasattr(user, 'instructor'):
                    return redirect('dashboard')
                else:
                    return redirect('/admin/')
            except Exception as e:
                print(f"Erreur lors de la redirection après connexion : {e}")
                messages.error(request, "Erreur interne. Veuillez réessayer.")
        else:
            messages.error(request, "Vos identifiants ne sont pas corrects.")
    else:
        messages.error(request, "Méthode non autorisée.")
    return redirect('login')


    
def deconnexion(request):
    logout(request)
    return redirect('login')
