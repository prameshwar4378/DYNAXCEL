from django.shortcuts import render,redirect
from WebAdmin.models import *
# Create your views here.
from django.contrib import messages

def index(request):
    gallery_images= PhotoGallery.objects.select_related().filter(is_show_on_home_page=True)
    data={
        'gallery_images':gallery_images,
    }
    
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic validation (you can customize this)
        if name and mobile and email and subject and message:
            Enquiry.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request,"Thank You...!") 
            return redirect('/')
        else:
            messages.error(request,"All fields are required")

    return render(request,"index.html",data)

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Basic validation (you can customize this)
        if name and mobile and email and subject and message:
            Enquiry.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request,"Thank You...!") 
            return redirect('/web/contact-us')
        else:
            messages.error(request,"All fields are required")
    return render(request,"contact_us.html")

def about_us(request):
    return render(request,"about_us.html")

def career(request):
    return render(request,"career.html")

def career_apply_job(request):
    return render(request,"career_apply_job.html")

def infrastructure(request):
    return render(request,"infrastructure.html")
def web_news(request):
    return render(request,"web_news.html")

def career(request):
    career_list=Career.objects.filter(is_publish=True).order_by('-id')
    return render(request,"career.html",{'career_list':career_list})

def career_apply_job(request,id):
    job_details=Career.objects.get(id=id)
    return render(request,"career_apply_job.html",{'job_details':job_details})

 
def create_career_application(request):
    if request.method == 'POST':
        career_id = request.POST.get('career_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES['resume']

        career=Career.objects.get(id=career_id)
        # Create a CareerApplication object and save the data
        application = CareerApplication(
            career=career,
            name=name,
            email=email,
            phone=phone,
            resume=resume  # File field will automatically handle the file path
        )
        application.save()
        messages.success(request,f'Application successfuly submited...!') 
        return redirect(f'/web/career_apply_job/{career_id}')


def sustainability(request):
    return render(request,"sustainability.html")

def certificates(request):
    return render(request,"web_certificates.html")

def web_photos_gallary(request):
    data=PhotoGallery.objects.all().select_related()
    return render(request,"web_photos_gallary.html",{'data':data})

def services_ASME_PED_Vessels(request):
    return render(request,"services_ASME_PED_Vessels.html")

def services_food_farma(request):
    return render(request,"services_food_farma.html")

def services_railway_metro(request):
    return render(request,"services_railway_metro.html")

def services_psa_based(request):
    return render(request,"services_psa_based.html")

def services_defence_equipements(request):
    return render(request,"services_defence_equipements.html")

def stainless_steel(request):
    return render(request,"services_stainless_steel.html")

def services_mining(request):
    return render(request,"services_mining.html")

def services_paper(request):
    return render(request,"services_paper.html")

def services_power(request):
    return render(request,"services_power.html")

def services_textiles(request):
    return render(request,"services_textiles.html")


