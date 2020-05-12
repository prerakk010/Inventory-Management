from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

# Display Devices 
def display_device(request,cls,head):
    items=cls.objects.all()
    context ={
        'items' : items,
        'header': head

    }
    return render(request, 'index.html',context)

def display_laptops(request):
    return display_device(request, Laptop,'Laptops')

def display_desktops(request):
    return display_device(request, Desktop,'Desktops')

def display_mobiles(request):
    return display_device(request, Mobile,'Mobiles')

# Add Device

def add_device(request, cls):
    if request.method == 'POST':
        form =cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= cls()
        return render(request,'add_new.html',{'form': form})

def add_laptop(request):
    return add_device(request, LaptopForm)


def add_desktop(request):
    return add_device(request, DesktopForm)


def add_mobile(request):
    return add_device(request, MobileForm)

# Edit Device

def edit_device(request,pk, model, cls):
    item = get_object_or_404(model,pk=pk)

    if request.method == 'POST':
        form= cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=cls(instance=item)
        return render(request, 'edit_item.html',{'form': form})

def edit_laptop(request,pk):
    return edit_device(request,pk, Laptop,LaptopForm)

def edit_desktop(request,pk):
    return edit_device(request,pk, Desktop,DesktopForm)

def edit_mobile(request,pk):
    return edit_device(request,pk, Mobile,MobileForm)

# Delete Device

def delete_device(request, pk, models):
    models.objects.filter(id=pk).delete()
    items= models.objects.all()
    context={
        'items':items
    }
    return render(request,'index.html',context)

def delete_laptop(request,pk):
    return delete_device(request,pk,Laptop)

def delete_desktop(request,pk):
    return delete_device(request,pk,Desktop)

def delete_mobile(request,pk):
    return delete_device(request,pk,Mobile)