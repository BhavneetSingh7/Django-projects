from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist

# Function to create verification keys
def get_vk(input_value):
    # Create a unique key for every unverified subscriber 
    # to be passed into the url of verification link
    val = input_value.split('@')
    return val[0]

# Function to send verification email
def send_verification_email(email_id):
    pass

# Function to check if client is already subscribed 
def check_duplicate_subscriber(email_id):
    pass

# Create your views here.
def index(request):
    form = CredsForm()
    if request.method == 'POST':
        vk = get_vk(request.POST['email_id'])
        subscriber = {
            'csrfmiddlewaretoken':request.POST['csrfmiddlewaretoken'],
            'email_id':request.POST['email_id'],
            'verified':False,
            'verify_key':vk,
        }
        form = CredsForm(subscriber)
        if form.is_valid():
            form.save()
            # send_verification_email(subscriber['email_id'])
        return redirect('newsletter:newsletter_check')
    
    context = {'form':form}
    return render(request,'newsletter/index.html',context)

def check(request):
    # return HttpResponse('We have sent you a verification email!.\nPlease click on the link in that email to verify yourself.')
    return render(request,'newsletter/check.html')

def verification(request,subscriber,verify_key):
    try:
        sub = Creds.objects.get(email_id=subscriber,verify_key=verify_key)
        sub.verified = True
        sub.save()
    except ObjectDoesNotExist:
        return HttpResponse('Verification Failed')
    return render(request,'newsletter/verification.html')

def unsubscribe(request,subscriber,verify_key):
    sub = Creds.objects.get(email_id=subscriber,verify_key=verify_key)
    sub.delete()
    return render(request,'newsletter/unsubscribe.html',context={'email_id':subscriber})
