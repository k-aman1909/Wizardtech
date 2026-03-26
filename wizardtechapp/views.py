from django.shortcuts import render,HttpResponse
from django.template import loader

def homepage(request):
    return render(request, 'wizardtechapp/wizard.html')
def verification(request):
    return render(request,'verificationform.html')
def certificate(request):
    return render(request,'certificate-verification.html')
def marksheet(request):
    return render(request,'marksheet-verify.html')
def typing(request):
    return render(request,'typing-verify.html')
def syllabuspage(request):
    return render(request,'syllabuspage.html')
def aboutus(request):
    return render(request,'aboutwizard.html')
def gallery(request):
    return render(request,'gallerywizard.html')
def certificatesample(request):
    return render (request,'certificate-sample.html')
def marksheetsample(request):
    return render (request,'mark-sheetwizard.html')
def icard(request):
    return render (request,'i-cardwizard.html')
