from django.shortcuts import render
from .models import Note
def homepage(request):
    return render(request,'home.html')
def notes(request):
    context ={ }
    codecontext ={ }
    system=request.POST.get('notes',None)
    notes=Note.objects.filter(SBSKEY=system).order_by('subject_code','module_no')
    i=1
    for note in notes:
        if note.subject_code not in codecontext.values():
            if note.subject_name not in context.values():
                context["subject"+str(i)]=note.subject_name
                codecontext["subject"+str(i)]=note.subject_code
                i=i+1
    s=list(context.values())
    subcode=list(codecontext.values())
    context['code']=subcode
    context['notes']=notes
    context['mainlist']=zip(s,subcode)
    return render(request,'notes.html',context)

def handler404(request,exception):
    return render(request, '404.html', locals())
