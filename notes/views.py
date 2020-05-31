from django.shortcuts import render
from .models import Note
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
def homepage(request):
  #  a,b=gd_storage.listdir("google drive folder-(API)")       
  #  print(a,b)#gives o/p a=list of directries and b=list of files 
    return render(request,'home.html')
def notes(request):
    context ={ }
    codecontext ={ }
    system=request.POST.get('notes',None)
    notes=Note.objects.filter(SBSKEY=system).order_by('subject_code','module_no')
    i=1
    sem=''
    scheme=''
    branch=''
    for note in notes:
        if note.subject_code not in codecontext.values():
            if note.subject_name not in context.values():
                context["subject"+str(i)]=note.subject_name
                codecontext["subject"+str(i)]=note.subject_code
                sem=note.sem
                scheme=note.scheme
                branch=note.branch
                i=i+1           
    s=list(context.values())
    subcode=list(codecontext.values())
    context['code']=subcode
    context['notes']=notes
    context['mainlist']=zip(s,subcode)
    context['subname']=s
    context['sem']=sem
    context['scheme']=scheme
    context['branch']=branch
    return render(request,'notes.html',context)
   
def viewnotes(request):
    context={ }
    system=request.POST.get('viewnotes',None)
    path=gd_storage.url(system)
    context['url']=path
    return render(request,'view.html',context) 

def handler404(request,exception):
    return render(request, '404.html', locals())


