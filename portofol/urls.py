from django.contrib import admin
from django.urls import path
from portofol.views import generate_cv,generate_resume,mycv
app_name="portofol"
urlpatterns = [

    path('cv/', generate_cv),
    path('resume/', generate_resume),
    path('', mycv)
]