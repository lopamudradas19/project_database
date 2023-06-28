from django.db import models

# Create your models here.
class country(models.Model):
    c_id=models.IntegerField(primary_key=True,max_length=100)
    c_name=models.CharField(max_length=100)
    def __str__(self):
        return self.c_name

class state(models.Model):
    s_id=models.IntegerField(max_length=100)
    s_name=models.CharField(max_length=100)
    c_id=models.ForeignKey(country,on_delete=models.CASCADE)
    def __str__(self):
        return self.s_name
    
