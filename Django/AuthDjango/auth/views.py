from django.shortcuts import render
from auth import forms
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
'''def login(request):
    loginForm = forms.LoginForm()
    error = None

    #now writing code for the case when user presses the login button to POST his login credentials
    if request.method == 'POST':
        loginForm = forms.LoginForm(request.POST)
        if loginForm.is_valid(): 
            #extract username and password from the form
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            #check if the credentials are valid
            user = authenticate(username = username, password = password)
            if user: #means user object is returned if the authentication is successful
                print(user)
                auth_login(request, user)   
                return HttpResponseRedirect('/')
            else:
                error = "Invalid username or password"


    context ={
        'form': loginForm,
        'error': error
    }
    return render(request, 'auth/login.html', context)'''

    #now implementing all the above function by using generic views
class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    next = '/' # this next objects tells where to redirect to after user gives the login request(by default it is '/')

class Logout(LogoutView):
    pass