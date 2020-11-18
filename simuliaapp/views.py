from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SereliaForm
from .models import Serelia, Contact
import datetime

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
def sereliaList(request, seed_type=None):
    seed_type_temp = ""
    if (seed_type==None):
        seed_type_temp="All"
        serelias = Serelia.objects.all()
    else:
        seed_type_temp = seed_type
        serelias = Serelia.objects.filter(seed_type=seed_type)
    return render(request,'pages/serelia_list.html',{'serelias':serelias, 'seed_type':seed_type_temp })  

@login_required
def sereliaCreate(request):  
    if request.method == "POST":  
        form = SereliaForm(request.POST, request.FILES)
        if form.is_valid():  
            try: 
                serelia = form.instance
                serelia.save()
                serelia.locationid = 'L'+str(10000+serelia.id)
                serelia.save()
                messages.success(request, "Data berhasil disimpan. "+str(serelia.locationid))
                return redirect('serelia_list')  
            except Exception as e:  
                messages.error(request, "Data gagal disimpan.\n"+str(e))
                return redirect('serelia_list')  
    else:  
        form = SereliaForm()  
    return render(request,'pages/serelia_create.html',{'form':form})  

@login_required
def sereliaDelete(request, id):
    serelia = Serelia.objects.get(id=id)
    try:
        serelia.delete()
        messages.success(request, "Data berhasil dihapus.")
    except:
        messages.error(request, "Data gagal dihapus.")
    return redirect('serelia_list')

@login_required
def sereliaDetail(request, id):
    serelia = Serelia.objects.get(id=id)
    return render(request, 'pages/serelia_detail.html', {'serelia':serelia})

@login_required
def contact(request):
    contact = Contact.objects.first()
    return render(request, 'pages/contact.html', {'contact':contact})