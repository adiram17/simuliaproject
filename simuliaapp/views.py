from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SereliaForm, ProcessingForm, WarehousestockForm
from .models import Serelia, Contact, Processing, Warehousestock
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
def contact(request):
    contact = Contact.objects.first()
    return render(request, 'pages/contact.html', {'contact':contact})

@login_required
def sereliaList(request, seed_type=None):
    seed_type_temp = ""
    if (seed_type==None):
        seed_type_temp="Semua"
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
def processingList(request):
    processings = Processing.objects.all()
    return render(request,'pages/processing_list.html',{'processings':processings})  

@login_required
def processingCreate(request):  
    if request.method == "POST":  
        form = ProcessingForm(request.POST, request.FILES)
        if form.is_valid():  
            try: 
                processing = form.instance
                processing.save()
                processing.processingid = 'P'+str(10000+processing.id)
                processing.save()
                messages.success(request, "Data berhasil disimpan. "+str(processing.processingid))
                return redirect('processing_list')  
            except Exception as e:  
                messages.error(request, "Data gagal disimpan.\n"+str(e))
                return redirect('processing_list')  
    else:  
        form = ProcessingForm()  
    return render(request,'pages/processing_create.html',{'form':form})  

@login_required
def processingDelete(request, id):
    processing = Processing.objects.get(id=id)
    try:
        processing.delete()
        messages.success(request, "Data berhasil dihapus.")
    except:
        messages.error(request, "Data gagal dihapus.")
    return redirect('processing_list')

@login_required
def processingDetail(request, id):
    processing = Processing.objects.get(id=id)
    return render(request, 'pages/processing_detail.html', {'processing':processing})

@login_required
def warehousestockList(request):
    warehousestocks = Warehousestock.objects.all()
    return render(request,'pages/warehousestock_list.html',{'warehousestocks':warehousestocks})  

@login_required
def warehousestockCreate(request):  
    if request.method == "POST":  
        form = WarehousestockForm(request.POST, request.FILES)
        if form.is_valid():  
            try: 
                warehousestock = form.instance
                warehousestock.save()
                warehousestock.stockid = 'S'+str(10000+warehousestock.id)
                warehousestock.save()
                messages.success(request, "Data berhasil disimpan. "+str(warehousestock.stockid))
                return redirect('warehousestock_list')  
            except Exception as e:  
                messages.error(request, "Data gagal disimpan.\n"+str(e))
                return redirect('warehousestock_list')  
    else:  
        form = WarehousestockForm()  
    return render(request,'pages/warehousestock_create.html',{'form':form})  

@login_required
def warehousestockDelete(request, id):
    warehousestock = Warehousestock.objects.get(id=id)
    try:
        warehousestock.delete()
        messages.success(request, "Data berhasil dihapus.")
    except:
        messages.error(request, "Data gagal dihapus.")
    return redirect('warehousestock_list')

@login_required
def warehousestockDetail(request, id):
    warehousestock = Warehousestock.objects.get(id=id)
    return render(request, 'pages/warehousestock_detail.html', {'warehousestock':warehousestock})
