from django.db import models
# Create your models here.

class Note(models.Model):
    module_no=models.CharField(max_length=3,default='',help_text=u"select the MODULE NUMBER")
    upload_file=models.FileField(help_text="UPLOAD CORRECT FILE         NOTE:U CANT CHANGE AFTER UPLOADING",upload_to='files/')
    subject_name=models.CharField(help_text="ENTER THE SUBJECT NAME",max_length=30,default='')
    added_by =models.CharField(help_text="ENTER YOUR NAME",max_length=10,default='')
    module_name=models.CharField(help_text="ENTER MODULE NAME",max_length=40,default='')
    subject_code=models.CharField(help_text="ENTER subject code",max_length=20,default='')
    scheme=models.CharField(help_text="choose the scheme",max_length=10,default='',choices=[('2017','2017'),('2018','2018')])
    branch=models.CharField(help_text="choose branch",max_length=100,default='',choices=[('cs/IS', 'cs/IS'),('EC','EC'),('civil','civil'),('mech','mech'),('1styear','1styear')])
    sem=models.CharField(help_text="choose the sem",max_length=10,default='',choices=[('3','3'),('4','4'),('5','5'),('6','6')])
    SBSKEY=models.CharField("SBSKEY",max_length=30,blank=False,editable=False)

    def save(self, *args, **kwargs):
        self.SBSKEY= self.scheme + self.branch + self.sem
        self.subject_code=self.subject_code.lower()
        self.subject_name=self.subject_name.lower()
        super(Note, self).save(*args, **kwargs)
    def __str__(self):
         return self.subject_name+" Module  "+self.module_no +"    ADDED BY: "+self.added_by+self.SBSKEY

