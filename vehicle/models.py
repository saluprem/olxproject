from django.db import models

# Create your models here.
class vehicles(models.Model):
     name=models.CharField(max_length=200)
     model=models.CharField(max_length=200)
     year=models.IntegerField()
     price=models.IntegerField()
     owner=models.CharField(max_length=200)
     mob=models.IntegerField()
     image=models.ImageField(upload_to="images",null=True)
     def __str__(self):
          return self.name
     
