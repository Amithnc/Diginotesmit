from django.shortcuts import render
from django.http import HttpResponse 
from .models import Note
from array import *
import string
def homepage(request):
    return render(request,'home.html')    
def notes(request):
    context ={ }
    system=request.POST.get('system',None)
    notes=Note.objects.filter(branch_sem_id=system)
    i=1
    for note in notes:
        if note.subject_name not in context.values():
            context["subject"+str(i)]=note.subject_name
            i=i+1
    s=list(context.values())
    context['subject']=s 
    context['notes']=notes
                               
    return render(request,'notes.html',context)
    

