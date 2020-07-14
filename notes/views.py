from django.shortcuts import render
from .models import Note
from gdstorage.storage import GoogleDriveStorage
gd_storage = GoogleDriveStorage()
def homepage(request):
    return render(request,'home.html')
def notes(request):
    context ={ }
    codecontext ={ }
    system=request.POST.get('notes',None)
    notes=Note.objects.filter(SBSKEY=system).order_by('subject_code','module_no')
    year=system[:4]
    system=system[4:]
    branch=['cs/IS','mech','civil','EC']
    temp=system[-1:]
    brnch=''
    ch=''
    if temp.isdigit():
        for i in system:
            ch=ch+i
            if ch in branch:
                brnch=(ch)
    else:
        brnch='1styear'
        temp=system[-7:]
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
    context['subname']=s
    context['sem']=temp
    context['scheme']=year
    context['branch']=brnch
    return render(request,'notes.html',context)

def viewnotes(request):
    context={ }
    system=request.POST.get('viewnotes',None)
    path=gd_storage.url(system)
    context['url']=path
    return render(request,'view.html',context)

def handler404(request,exception):
    return render(request, '404.html', locals())


