from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Note, ApiToken
from .forms import NoteForm
from .tokens import create_api_token


# Registration page view
def register(request):
    if request.method == 'POST':
        # Retrieving form data
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        # Validating form data
        if password1 == password2:
            # On successfull validation create user and other credentials
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            og_token_value = create_api_token()
            create_og_api_token = ApiToken(user=user,key=og_token_value,og_key=True)
            create_og_api_token.save()
            return redirect('notes:login')
        else:
            return render(request,'notes/register.html', {'failed':'Failed'})
    return render(request,'notes/register.html', {'failed':''})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('notes:notes_list')
        else:
            messages.info(request,'Incorrect username or password')
            return redirect('notes:login')
    return render(request,'notes/login.html')

def user_logout(request):
    logout(request)
    return redirect('notes:login')

# Content views - CRUD functionality
@login_required(login_url='notes:login')
def notes_list(request):
    content = Note.objects.filter(user=request.user)
    if request.method == 'POST':
        note = Note(user=request.user,title=request.POST['title'])
        note.save()
        return redirect('notes:notes_list')
    data = {
        'content':content,
    }
    return render(request,'notes/list.html',context=data)

@login_required(login_url='notes:login')
def note_detail(request,pk):
    content = Note.objects.get(id=pk)
    data = {
        'content':content,
    }
    return render(request,'notes/detail.html',context=data)

@login_required(login_url='notes:login')
def note_update(request,pk):
    content = Note.objects.get(id=pk)
    form = NoteForm(instance=content)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=content)
        if form.is_valid:
            form.save()
            return redirect('notes:notes_list')
    data = {
        'content':content,
        'form':form
    }
    return render(request,'notes/update.html',context=data)

@login_required(login_url='notes:login')
def note_delete(request,pk):
    content = Note.objects.get(id=pk).delete()
    print(content)
    return redirect('notes:notes_list')

# Landing Page
def index(request):
    return render(request,'notes/base.html')