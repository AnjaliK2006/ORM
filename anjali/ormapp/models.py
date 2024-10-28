from django.db import models
from django.contrib import admin
class loan(models.Model):
    Name=models.CharField(max_length=50)
    Accno=models.IntegerField(primary_key="Accno")
    Amount=models.IntegerField()
    Interest=models.FloatField()
    Startdate=models.DateField()
    Phoneno=models.IntegerField()
    Email=models.EmailField()
    Enddate=models.DateField()

class loanAdmin(admin.ModelAdmin):
    list_display=('Name','Accno','Amount','Interest','Startdate','Phoneno','Email','Enddate')     



