
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.

def index(request):
    if "user_id" in request.session:
        return redirect ('/jobs')
    else:

        return render(request, "index.html")

def reg_User(request):
    errors = User.objects.user_validations(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if User.objects.filter(Email = request.POST['email']).first():
        
        print('User already exists')
        return redirect('/')


    password = request.POST['pwd']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)
    
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pwd = pw_hash

        

        
    user1 = User.objects.create(First_name = fname, Last_name = lname, Email = email, Password = pwd)
            
    request.session['user_id'] = user1.id
    return redirect('/jobs')


def processlogin(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user_matching_email = User.objects.filter(Email = request.POST['email']).first()
    print(user_matching_email)

    if user_matching_email is not None:
        if bcrypt.checkpw(request.POST['pwd'].encode(), user_matching_email.Password.encode()):
            request.session['user_id'] = user_matching_email.id
            return redirect('/jobs')
            
        else: 
            print('password incorrect')
            messages.add_message(request, messages.ERROR, 'Invalid Credentials.')
            return redirect ('/')
    else:
        messages.error(request, "No User Found")
        print('no user found')
        return redirect('/')



def display_congrats(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print(request.session.get('user_id'))
    context = {
        'thisUser': User.objects.get(id = request.session['user_id']),
        
    }
    return render(request, "displayreguser.html", context)


def logout(request):
    request.session.clear()
    return redirect('/')


