from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("This is my homepage")
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def skill(request):
    return render(request,'skills.html')

def project(request):
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def resume(request):
    return render(request,'resume.html')