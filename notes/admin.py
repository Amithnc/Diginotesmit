
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from datetime import datetime
import csv, sys, os
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Note
from django.contrib.auth.hashers import make_password
''' just for UI of the ADMIN  '''
admin.site.register(Note)
admin.site.index_title="add notes"
admin.site.site_title="notes@mit"
admin.site.site_header="notes administration"

'''for importing bulk users from CSV file'''
project_dir = "C:\project\demo-project"
sys.path.append(project_dir)
User = get_user_model()
file = 'import.csv'
'''for sending the email'''
SenderAddress='mit.enotes@gmail.com'
password="password for email"


def row_count(filename):
    with open(filename) as file:
        return sum(1 for _ in file)

reader = csv.reader(open(file), delimiter=",")
last_line_number = row_count(file)
for row in reader:
    if last_line_number == reader.line_num:
            break
    usrname =row[0]
    upper_pass=usrname.upper()+"@MIT"
    email=row[2]
    grp=row[4]
    User.objects.get_or_create(username=usrname, is_staff=True) 
    u = User.objects.get(username=usrname)
    u.set_password(upper_pass)
    u.email=email
    group = Group.objects.get(name=grp)
    u.groups.add(group)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(SenderAddress, password)
    msg = "hello :) below are the credentials that you need to upload the notes to our website"+"\n"+"your username is:\t"+usrname+"\nyour password is:\t"+upper_pass+"\n link to the website:\t amithnc.pythonanywhere.com/moniter"+"\n\n"+"NOTE:please change your  password once u login\n"+"\n\n"+"-MIT ERP TEAM"
    subject = "MIT NOTES login credentials"
    body = "Subject: {}\n\n{}".format(subject,msg)
    server.sendmail(SenderAddress, email, body)
    print("created and mail sent to",usrname)
    u.save()
server.quit()        


class NoteAdmin(admin.ModelAdmin):
'''automatically save added_by field to current logged in user'''

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(added_by=request.user)

''' for better view of admin dashboard'''

    list_display = ('subject_name', 'branch','sem','module_no','added_by',)
    list_filter = ('branch',)
    search_fields = ('subject_name', 'sem')
    readonly_fields = ('SBSKEY',)
    ordering = ('branch',)

'''filter notes added by the user who logs in'''

    def save_model(self, request, obj, form, change):
        if not change:           
            obj.added_by = request.user
        obj.save()    


admin.site.register (Note, NoteAdmin)





