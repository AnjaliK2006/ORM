# Ex02 Django ORM Web Application
## Date: 28/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2024-10-26 192433.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

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

admin.py

from django.contrib import admin
from.models import loan,loanAdmin
admin.site.register(loan,loanAdmin)

```
  
## OUTPUT
![alt text](<Screenshot 2024-10-26 190128.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
