from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SereliaForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'pages/home.html', {})

# Create your views here.
@login_required
def profile(request):
    return render(request, 'user/profile.html', {})

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Update Password Success.')
            return redirect('home')
        else:
            messages.error(request, 'Update Password Canceled.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })


@login_required
def sereliaList(request):  
    return render(request,'pages/serelia_list.html',{})  

@login_required
def sereliaCreate(request):  
    if request.method == "POST":  
        form = SereliaForm(request.POST)  
        if form.is_valid():  
            try:  
                #form.save() 
                #model = form.instance
                messages.success(request, "Data belum bisa ditambahkan masih inprogress development")
                return redirect('serelia_list')  
            except:  
                messages.error(request, "Data belum bisa ditambahkan masih inprogress development")
                pass  
    else:  
        form = SereliaForm()  
    return render(request,'pages/serelia_create.html',{'form':form})  