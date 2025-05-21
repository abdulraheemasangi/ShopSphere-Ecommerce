from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout

# Create your views here.

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request,'user_login.html',{'loginnav':True})

def user_register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():        
            messages.error(request, 'Username already exists. Please choose another one.')
            return redirect('user_register')

        user=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=username)
        user.set_password(password)
        user.save()
        messages.success(request,'Account created successfully. Please login.')
        return redirect('user_login')


    return render(request,'user_register.html',{'loginnav':True})



def profile(request):

    return render(request,'profile.html',{'profile_nav':True})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('user_login')

def changepass(request):
    if request.method == 'POST':
        newpassword = request.POST['password']
        user = request.user
        user.set_password(newpassword)
        user.save()
        messages.success(request, 'Password Changed successfully.')
        return redirect('profile')
    
    return render(request,'changepass.html',{'profile_nav':True})



def update_profile(request):

    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')  

    return render(request, 'update_profile.html', {'user': user})