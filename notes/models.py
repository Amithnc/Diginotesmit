from django.db import models
# Create your models here.
class Note(models.Model):
    module_no=models.CharField(max_length=3,default='',help_text=u"select the MODULE NUMBER")
    upload_file=models.FileField(help_text="UPLOAD CORRECT FILE         NOTE:U CANT CHANGE AFTER UPLOADING",upload_to='files/')
    subject_name=models.CharField(help_text="ENTER THE SUBJECT NAME",max_length=30,default='')
    added_by =models.CharField(help_text="ENTER YOUR NAME",max_length=10,default='')
    module_name=models.CharField(help_text="ENTER MODULE NAME",max_length=40,default='')
    branch_and_sem=models.CharField(help_text="choose branch and sem",max_length=100,default='',choices=[('cs/IS-sem3', 'cs/IS-sem3'),('cs/IS-sem4','cs/IS-sem4'),('cs/IS-sem5','cs/IS-sem5'),('cs/IS-sem6','cs/IS-sem6'),('ec-sem3', 'ec-sem3'),('ec-sem4','ec-sem4'),('ec-sem5','ec-sem5'),('ec-sem6','ec-sem6'),('civil-sem3', 'civil-sem3'),('civil-sem4','civil-sem4'),('civil-sem5','civil-sem5'),('civil-sem6','civil-sem6'),('mech-sem3', 'mech-sem3'),('mech-sem4','mech-sem4'),('mech-sem5','mech-sem5'),('mech-sem6','mech-sem6')])

    def __str__(self):
         return self.subject_name+" Module  "+self.module_no +"    ADDED BY: "+self.added_by+self.branch_and_sem

