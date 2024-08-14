from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is Created')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()
            # return HttpResponse('Webpage is Created')
            webpage=Webpage.objects.all()
            d1={'webpage':webpage}
            return render(request,'display_webpages.html',d1)

    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO=AccessForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessForm(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            au=AFDO.cleaned_data['author']
            dt=AFDO.cleaned_data['date']

            NO=Webpage.objects.get(name=na)
            AO=AccessRecord.objects.get_or_create(name=NO,author=au,date=dt)[0]
            AO.save()
            return HttpResponse('Access Record is created')


    return render(request,'insert_access.html',d)


def insert_topic_mf(request):
    ETMFO=TopicModelForm()
    d={'ETMFO':ETMFO}
    if request.method=='POST':
        TMFDO=TopicModelForm(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('topic is created')
    return render(request,'insert_topic_mf.html',d)


def insert_web_mf(request):
    EWMFO=WebpageModelForm()
    d={'EWMFO':EWMFO}
    if request.method=='POST':
        WMFDO=WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse('webpage is created')
    return render(request,'insert_web_mf.html',d)


def insert_Access_mf(request):
    EAMFO=AccessModelForm()
    d={'EAMFO':EAMFO}
    if request.method=="POST":
        AMFDO=AccessModelForm(request.POST)
        if AMFDO.is_valid():
            AMFDO.save()
            return HttpResponse("donnnnnnnnnnnnnne")
    return render(request,'insert_Access_mf.html',d)


