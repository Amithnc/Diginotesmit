from django.shortcuts import render
from .models import Note
def homepage(request):
    return render(request,'home.html')
def notes(request):
    context ={ }
    system=request.POST.get('notes',None)
    notes=Note.objects.filter(branch_and_sem=system)
    i=1
    for note in notes:
        if note.subject_name not in context.values():
            context["subject"+str(i)]=note.subject_name
            i=i+1
    s=list(context.values())
    context['subject']=s
    context['notes']=notes

    return render(request,'notes.html',context)


