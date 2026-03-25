from django.contrib import admin
from django.urls import path,include
from wizardtechapp import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('verification/',views.verification, name='verification'),
    path('certificate-verification/',views.certificate, name='certificate-verification'),
    path('syllabuspage/',views.syllabuspage,name='syllabuspage'),
    path('marksheet-verify/',views.marksheet,name='marksheet-verify'),
    path('typing-verify/',views.typing,name='typing-verify'),
    path('aboutwizard/',views.aboutus,name='aboutus'),
    path('gallerywizard/',views.gallery,name='gallery'),
    path('certificate-sample/',views.certificatesample,name='certificate'),
    path('mark-sheetwizard/',views.marksheetsample,name='marksheet'),
    path('i-cardwizard/',views.icard,name='icard'),
    
]
