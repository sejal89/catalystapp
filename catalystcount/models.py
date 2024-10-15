from django.db import models

# Create your models here.

class adduser(models.Model):
    user_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    active=models.CharField(max_length=50)
    
    def __str__(self): 
	    return self.user_name 

class person(models.Model):
    person_id=models.IntegerField()
    name=models.CharField(max_length=50)
    domain=models.CharField(max_length=50, default='DEFAULT VALUE')
    year_founded=models.IntegerField()
    industry=models.CharField(max_length=50)
    size_range=models.IntegerField()
    locality=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    linkedin_url=models.CharField(max_length=50)
    current_empl_estimate=models.IntegerField()
    total_employee_estimate=models.IntegerField()
    def __str__(self): 
	    return self.person_id 


class File(models.Model):
    file = models.FileField(upload_to="excel") 