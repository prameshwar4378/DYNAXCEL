from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render,redirect,get_object_or_404
from WebAdmin.models import *
# Create your views here.
from django.contrib import messages
import threading


def index(request):
    gallery_images= PhotoGallery.objects.select_related().filter(is_show_on_home_page=True)
    news = News.objects.select_related().order_by("-id")[:5]

    data={
        'gallery_images':gallery_images,
        'news':news,
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



def send_email_in_background(email_message):
    try:
        email_message.send()
    except Exception as e:
        print(f"Error sending email: {e}")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and mobile and email and subject and message:
            # Save the enquiry in the database
            Enquiry.objects.create(
                name=name,
                mobile=mobile,
                email=email,
                subject=subject,
                message=message
            )

            # Prepare email content
            email_subject = f"New Enquiry from {name}: {subject}"
            email_body = (
                f"Dear Team,\n\n"
                f"You have received a new enquiry from your website.\n\n"
                f"Details:\n"
                f"Name: {name}\n"
                f"Mobile: {mobile}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n"
                f"{message}\n\n"
                f"Regards,\n"
                f"Website Enquiry System"
            )

            # Configure the email
            email_message = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=['ims@dynaxcel.com'],  # Replace with the appropriate email address -- sales@dynaxcel.com
            )

            # Send the email in a separate thread to avoid blocking
            email_thread = threading.Thread(target=send_email_in_background, args=(email_message,))
            email_thread.start()

            # Success message to the user
            messages.success(request, "Thank You! Your enquiry has been submitted successfully.")
        else:
            messages.error(request, "All fields are required")

        return redirect('/web/contact-us')

    return render(request, "contact_us.html")




def about_us(request):
    return render(request,"about_us.html")

def career(request):
    return render(request,"career.html")

def career_apply_job(request):
    return render(request,"career_apply_job.html")

def infrastructure(request):
    return render(request,"infrastructure.html")

 
def web_news(request):
    news=News.objects.select_related().order_by('-id')
    return render(request,"web_news.html",{'news':news})

def web_news_details(request,id):
    try:
        latest_news = News.objects.select_related().order_by('-id')[:10]
        news_details = get_object_or_404(News, id=id)
        photos_videos = NewsPhotosVideos.objects.filter(news=news_details)   

        video_data=[]
        for embed_link in photos_videos:
            embed_url= embed_link.video_link
            if embed_url:
                video_id=extract_video_id(embed_url)
                if video_id:
                    video_data.append(
                        {"thumbnail_url":f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                        "video_url":f"https://www.youtube.com/embed/{video_id}",
                        "id":embed_link.id} 
                    )
        data={"latest_news":latest_news,
              "news_details": news_details, 
              'video_data': video_data,
              'photos_videos':photos_videos
              
              }
        return render(request, "web_news_details.html", data)
    except Exception as e: 
        return render(request, "404.html", status=404)


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
        resume = request.FILES.get('resume')

        # Check if the resume was uploaded
        if resume is None:
            messages.error(request, "Error: No resume uploaded.")
            return redirect(f'/web/career_apply_job/{career_id}')

        career = Career.objects.get(id=career_id)

        # Create and save the CareerApplication object
        application = CareerApplication(
            career=career,
            name=name,
            email=email,
            phone=phone,
            resume=resume
        )
        application.save()

        # Prepare email content
        subject = f"Application For | {career.title}"
        body = (
            f"Dear HR,\n\n"
            f"You have received a new job application.\n\n"
            f"Details:\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Applied for: {career.title}\n"
            f"Location: {career.location}\n\n"
            f"Please find the attached resume for more details.\n\n"
            f"Regards,\n"
            f"Dynaxcel Careers"
        )

        # Configure the email
        email_message = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['hr@dynaxcel.com'],  # Use your HR email
        )

        # Read resume content and attach to the email
        try:
            # Attach the resume with a check for size
            if resume.size == 0:
                messages.error(request, "Error: Resume is empty.")
                return redirect(f'/web/career_apply_job/{career_id}')

            # Attach the resume using 'with' to ensure the file is properly handled
            with resume.open('rb') as resume_file:
                email_message.attach(resume.name, resume_file.read(), resume.content_type)

        except Exception as e:
            print(f"Error reading resume: {e}")
            messages.error(request, "Error reading the resume file.")
            return redirect(f'/web/career_apply_job/{career_id}')

        # Send the email in a separate thread to avoid blocking
        email_thread = threading.Thread(target=send_email_in_background, args=(email_message,))
        email_thread.start()

        messages.success(request, 'Application submitted successfully!')

        # Redirect to the job application page
        return redirect(f'/web/career_apply_job/{career_id}')


 
def sustainability(request):
    return render(request,"sustainability.html")

def certificates(request):
    return render(request,"web_certificates.html")

def web_photos_gallary(request):
    data=PhotoGallery.objects.all().select_related()
    return render(request,"web_photos_gallary.html",{'data':data})
 
import re

def extract_video_id(embed_url):
    match = re.search(r"embed/([a-zA-Z0-9_-]+)", embed_url)
    if match:
        return match.group(1)
    return None


def web_videos_gallary(request): 
    data = VideoGallery.objects.all()
    video_data=[]
    for embed_link in data:
        embed_url= embed_link.video_link
        if embed_url:
            video_id=extract_video_id(embed_url)
        
            if video_id:
                video_data.append(
                    {"thumbnail_url":f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg",
                    "video_url":f"https://www.youtube.com/embed/{video_id}",
                    "id":embed_link.id} 
                )
  
    return render(request, 'web_video_gallary.html', {"video_data":video_data})


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