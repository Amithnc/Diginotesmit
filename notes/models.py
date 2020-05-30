from django.db import models
from gdstorage.storage import GoogleDriveStorage
from django.contrib.auth.models import User
gd_storage = GoogleDriveStorage()
class Note(models.Model):
    module_no=models.CharField(max_length=6,default='',help_text="enter the MODULE NUMBE,u can even enter 1-5 for all moudle or modify on your need")
    notes_file=models.FileField(upload_to='googlefiles/', storage=gd_storage,help_text="please UPLOAD CORRECT FILE")
    subject_name=models.CharField(help_text="ENTER THE SUBJECT NAME",max_length=30,default='')
    added_by= models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,editable=False)
    module_name=models.CharField(help_text="ENTER MODULE NAME",max_length=50,default='')
    subject_code=models.CharField(help_text="ENTER subject code",max_length=10,default='')
    scheme=models.CharField(help_text="choose the scheme",max_length=10,default='',choices=[('2017','2017'),('2018','2018')])
    branch=models.CharField(help_text="choose branch",max_length=20,default='',choices=[('cs/IS', 'cs/IS'),('EC','EC'),('civil','civil'),('mech','mech'),('1styear','1styear')])
    sem=models.CharField(help_text="choose the sem",max_length=5,default='',choices=[('3','3'),('4','4'),('5','5'),('6','6')])
    external_link=models.URLField(max_length = 200,help_text="enter the url",default='',blank=True)
    SBSKEY=models.CharField("SBSKEY",max_length=30,blank=False,editable=False,help_text="this field will be auto poluted")

    def save(self, *args, **kwargs):
        self.SBSKEY= self.scheme + self.branch + self.sem
        self.subject_code=self.subject_code.lower()
        self.subject_name=self.subject_name.lower()
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
         return self.subject_name+" Module  "+self.module_no