from django.db import models
from django.conf import settings
# Create your models here.
def sample_view(request):
    current_user = request.user
class Note(models.Model):
    module_no=models.CharField(max_length=1,default='',help_text=u"ENTER THE MODULE NUMBER")
    upload_file=models.FileField(help_text="UPLOAD CORRECT FILE         NOTE:U CANT CHANGE AFTER UPLOADING",upload_to='files/')
    subject_name=models.CharField(help_text="ENTER THE SUBJECT NAME",max_length=10,default='')
    added_by =models.CharField(help_text="ENTER YOUR NAME",max_length=10,default='')   
    module_name=models.CharField(help_text="ENTER MODULE NAME",max_length=40,default='')

    def __str__(self):
         return self.subject_name+" Module  "+self.module_no +"    ADDED BY: "+self.added_by

