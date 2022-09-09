from django.shortcuts import render,redirect
import uuid
from .models import Link
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request,'shortner/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Link(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Link.objects.get(uuid=pk)
    return redirect(url_details.link)
    #return redirect('https://'+url_details.link)