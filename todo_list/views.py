from django.shortcuts import render, redirect
from .models import List
from .models import Subgroup
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

subgroups_XYZ = [
    {"name":"Amphibians",
        "organisms":[
            {"name":"Ambystoma mexicanum","common_name":"----"},
            {"name":"Xenopus laevis","common_name":"----"},
            {"name":"Xenopus tropicalis","common_name":"----"} ]
    },
    {"name":"Birds",
        "organisms":[
            {"name":"Anas platyrhynchos","common_name":"Mallard"},
            {"name":"Calypte anna","common_name":"Anna's hummingbird "},
            {"name":"Columba livia","common_name":"Rock dove, rock pigeon"},
            {"name":"Coturnix japonica","common_name":"Japanese quail"},
            {"name":"Falco peregrinus","common_name":"Peregrine falcon"},
            {"name":"Ficedula albicollis","common_name":"Collared flycatcher"},
            {"name":"Gallus gallus","common_name":"Red junglefowl"},
            {"name":"Meleagris gallopavo","common_name":"Wild turkey"},
            {"name":"Numida meleagris","common_name":"Helmeted guineafowl "},
            {"name":"Parus major","common_name":"Great tit"},
            {"name":"Passer domesticus","common_name":"House sparrow"},
            {"name":"Strigops habroptila","common_name":"Kakapo, night parrot, owl parrot"},
            {"name":"Taeniopygia guttata","common_name":"Zebra finch"}
            ]
    },
    {"name":"Mammals",
        "organisms":[
            {"name":"Bos indicus","common_name":"----"},
            {"name":"Bos taurus","common_name":"----"},
            {"name":"Bubalus bubalis","common_name":"----"},
            {"name":"Callithrix jacchus","common_name":"----"},
            {"name":"Capra aegagrus","common_name":"----"},
            {"name":"Capra hircus","common_name":"----"},
            {"name":"Cervus elaphus hippelaphus","common_name":"----"},
            {"name":"Chlorocebus sabaeus","common_name":"----"},
            {"name":"Equus caballus","common_name":"----"},
            {"name":"Felis catus","common_name":"----"},
            {"name":"Gorilla gorilla","common_name":"----"},
            {"name":"Homo sapiens","common_name":"----"},
            {"name":"Lycaon pictus","common_name":"----"}
        ]
    }
]


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            list = List.objects.all
            messages.success(request,("Item added to to-do list"))
            return render(request, 'home.html', {'list':list })
    else:
        list = List.objects.all
        return render(request, 'home.html', {'list':list })

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item deleted"))
    return redirect( 'home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    messages.success(request,("Item updated"))
    return redirect( 'home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    messages.success(request,("Item updated"))
    return redirect( 'home')

def edit(request, list_id):
    if request.method == "POST":
        item=List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,("Item has been edited"))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item })


def bioinfx(request):
    subgroups = Subgroup.objects.all
    list = List.objects.all
    return render(request, 'bioinfx.html', {'list':list, 'subgroups':subgroups})
