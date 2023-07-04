from django.shortcuts import render
from app.models import *
from django.db.models.functions import *
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse

def topic_form(request):
    if request.method =='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name is created')
    return render(request,'topic_form.html')


def Webpage_form(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method == 'POST':
        tn=request.POST['tn']
        name=request.POST.get('na')
        url=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('webpage form is created')
    return render(request,'Webpage_form.html',d)



def AccessRecord_form(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        name=request.POST['na']
        date=request.POST['da']
        author=request.POST['au']
        
        WO=Webpage.objects.get(name=name)
        WO.save()
        ARO=AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        ARO.save()
        return HttpResponse('AccessRecord created')

    return render(request,'AccessRecord_form.html',d)



def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method == 'POST':
        MSTS=request.POST.getlist('topic')
        RWOS=Webpage.objects.none()
        for i in MSTS:
            RWOS=RWOS| Webpage.objects.filter(topic_name=i)
        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)

    return render(request,'retrieve_webpage.html',d)