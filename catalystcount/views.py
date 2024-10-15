from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import FileResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import uploadfile,  BookForm
from .models import adduser, person, File
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
import csv 

def Addbuilder(request):
    if request.method=="POST":
        person_id = request.POST['person_id']
        name = request.POST['name']
        domain = request.POST['domain']
        year_founded = request.POST['year_founded']
        industry = request.POST['industry']
        size_range = request.POST['size_range']
        locality = request.POST['locality']
        country = request.POST['country']
        linkedin_url = request.POST['linkedin_url']
        current_empl_estimate = request.POST['current_empl_estimate']
        total_employee_estimate = request.POST['total_employee_estimate']
        new_emp = person(person_id=person_id, name=name, domain=domain, year_founded=year_founded, industry=industry, size_range=size_range, locality=locality, country=country, linkedin_url=linkedin_url, current_empl_estimate=current_empl_estimate, total_employee_estimate=total_employee_estimate)
        new_emp.save()
        return redirect("viewbuilder")
    else:
        return render(request, "builder.html")

def viewbuilder(request):
    context=person.objects.all()
    return render(request, "show.html", {'context':context})

def download_csv(request):
    # Create the HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies_sorted.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'domain','year founded', 'industry', 'size range', 'locality' ,'country', 'linkedin url', 'current employee estimate', 'total employee estimate'])  # Write header

    # Query your model data
    for obj in person.objects.all():
        writer.writerow([obj.person_id, obj.name, obj.domain, obj.year_founded, obj.industry, obj.size_range, obj.locality, obj.country, obj.linkedin_url, obj.current_empl_estimate, obj.total_employee_estimate])  # Write data rows

    return response

def Adduser(request):
    if request.method=="POST":
        user_name = request.POST['user_name']
        email_id = request.POST['email_id']
        active = request.POST['active']
        new_emp = adduser(user_name=user_name, email_id=email_id, active=active)
        new_emp.save()
        return redirect("viewdata")
    else:
        return render(request, "user.html")
       
def viewdata(request):
    users=adduser.objects.all()
    return render(request, "viewdata.html", {'users':users})

def fileupload(request):
    # Retrieve all Employee objects from the database
    objs = person.objects.all()
    data = []
    for obj in objs:
        data.append({
            "id": obj.person_id,
            "name": obj.name,
            "domain":obj.domain,
            "year founded": obj.year_founded,
            "size range": obj.industry,
            "locality": obj.size_range,
            "country": obj.country,
            "linkedin url": obj.linkedin_url,
            "current employee estimate": obj.current_empl_estimate,
            "total employee estimate": obj.total_employee_estimate
        })
    pd.DataFrame(data).to_excel('output.xlsx')
    return render(request, 'fileupload.html')








    
