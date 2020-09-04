from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request,'home.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc)
        contact.save('self')
    return render(request,'contact.html')
