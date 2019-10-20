from django.shortcuts import render
from django.http import HttpResponse 
from .models import Note
def homepage(request):
    return render(request,'home.html')    
def notes(request):
    notes=Note.objects
    return render(request,'cs-is.html',{'notes':notes})  

