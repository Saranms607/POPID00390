from django.db import models

# Create your models here.

class Doctors(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField(upload_to='pics')
     desc=models.TextField()

     def _str_(self):
        return self.name
     
class Medicine(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    