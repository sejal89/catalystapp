from django.urls import path
from . import views

urlpatterns = [
    path('Addbuilder/',views.Addbuilder,name="Addbuilder"), 
    path('viewbuilder/',views.viewbuilder,name="viewbuilder"),   
    path('fileupload/',views.fileupload,name="fileupload"),   
    path('Adduser/',views.Adduser,name="Adduser"),   
    path('viewdata/',views.viewdata,name="viewdata"),
    path('download-csv/', views.download_csv, name='download_csv'),

]