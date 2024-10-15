from django import forms
from .models import adduser, person

# for creating file input  

class uploadfile(forms.Form):  
    file = forms.FileField() 
    
class BookForm(forms.ModelForm): 
	class Meta: 
		model = adduser 
		fields = ['user_name', 'email_id', 'active'] 
  
# class PersonForm(forms.ModelForm): 
# 	class Meta: 
# 		model = person 
# 		fields = ['id', 'name', 'domain', 'year_founded', 'industry', 'size_range', 'locality', 'country', 'linkedin_url', 'current_empl_estimate', 'total_employee_estimate'] 

class UploadFileForm(forms.Form):
    file = forms.FileField()