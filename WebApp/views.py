from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def contact_us(request):
    return render(request,"contact_us.html")

def about_us(request):
    return render(request,"about_us.html")

def web_news(request):
    return render(request,"web_news.html")
def career(request):
    return render(request,"career.html")

def career_apply_job(request):
    return render(request,"career_apply_job.html")
