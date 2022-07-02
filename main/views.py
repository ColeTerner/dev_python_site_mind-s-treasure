from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.order_by("-title")
    return render(request,"main/index.html",{"title":"Main page of site","tasks":tasks})

def about(request):
    return render(request,"main/about.html")

def contacts(request):
    return render(request,"main/contacts.html")

def create(request):
    error=""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error="Форма была неверная"
    form=TaskForm()
    context = {
        'form': form
    }
    return render(request,"main/create.html",context)
