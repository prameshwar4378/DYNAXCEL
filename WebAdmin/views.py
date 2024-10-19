from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
from django.contrib.auth import login as authlogin, authenticate,logout as DeleteSession
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request): 
    lg_form=login_form() 
    if request.method=='POST': 
         
        if 'username' in request.POST: 
            username = request.POST.get('username', False)
            password = request.POST.get('password', False)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                authlogin(request,user) 
                return redirect('/admin/dashboard',{'user',user})
            else:
                lg_form=login_form()
                messages.info(request,'Opps...! User does not exist... Please try again..!')
        else:
            print("Login Missing")

    return render(request,'login.html',{'form':lg_form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    DeleteSession(request)
    return redirect('/accounts/login')

def dashboard(request):
    application_count = CareerApplication.objects.count()
    enquiry_count = Enquiry.objects.count()
    job_posted = Career.objects.count()
    news_posted = News.objects.count()    
    context = {
        'application_count' : application_count,
        'enquiry_count' : enquiry_count,
        'job_posted' : job_posted,
        'news_posted' : news_posted
    }

    return render(request,"admin_dashboard.html", context)


@login_required
def career_list(request):
    career_data = Career.objects.all()
    form = CareerForm()
    return render(request, 'career_list.html', {'career_data': career_data,'form': form})


def create_career(request):
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        vacancy = int(request.POST['vacancy'])
        desired_qualification = request.POST['desired_qualification']
        experience_required = request.POST['experience_required']
        career_description = request.POST['career_description']
        roles_responsibility = request.POST['roles_responsibility']
        skills_required = request.POST['skills_required']
        is_publish = request.POST['is_publish']

        if is_publish=="on":
            is_publish=True
        else:
            is_publish=False
 
        # Save the data to the database
        career = Career(
            title=title,
            location=location,
            vacancy=vacancy,
            desired_qualification=desired_qualification,
            experience_required=experience_required,
            career_description=career_description,
            roles_responsibility=roles_responsibility,
            skills_required=skills_required,
            is_publish=is_publish
        )
        career.save()

        return redirect('/admin/career_list') 


def update_career(request, id):
    career = get_object_or_404(Career, id=id)
    
    if request.method == 'POST':
        form = CareerForm(request.POST, instance=career)
        if form.is_valid():
            form.save()
            return redirect('/admin/career_list')  # Replace with your URL for listing careers
    else:
        form = CareerForm(instance=career)
    
    return render(request, 'update_career.html', {'form': form, 'career': career})

def delete_career(request,id):
    Career.objects.get(id=id).delete()
    return redirect("/admin/career_list")

@login_required
def job_application_list(request): 
    data = CareerApplication.objects.all().order_by('-id') 
    return render(request, 'job_application_list.html', {"data":data})

def delete_job_applicattion(request,id):
    CareerApplication.objects.get(id=id).delete()
    messages.success(request,"Application has been deleted...!")
    return redirect("/admin/job_application_list")


@login_required
def photo_gallery_list(request): 
    data = PhotoGallery.objects.all()
    form = PhotoGalleryForm()
    return render(request, 'admin_photo_gallery_list.html', {'form': form, "data":data})


def create_photo_for_gallery(request):
    if request.method == 'POST':
        form = PhotoGalleryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Photo Added Success")
            return redirect('/admin/photo_gallery_list') 
        else:
            messages.error(request,"Form is not valid")
            return redirect('/admin/photo_gallery_list') 
             # Assuming you have a URL named 'list' for listing events
    else: 
            messages.error(request,"Form is not valid")
            return redirect('/admin/photo_gallery_list')  # Assuming you have a URL named 'list' for listing events

 
def delete_photo_from_gallery(request,id):
    PhotoGallery.objects.get(id=id).delete()
    return redirect("/admin/photo_gallery_list")



import re

def extract_video_id(embed_url):
    match = re.search(r"embed/([a-zA-Z0-9_-]+)", embed_url)
    if match:
        return match.group(1)
    return None




def video_gallery_list(request): 
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
    form = VideoGalleryForm()
    return render(request, 'admin_video_gallary_list.html', {'form': form, "video_data":video_data})


def create_video_for_gallery(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid(): 
            video_link = form.cleaned_data.get('video_link')
            video_id=extract_video_id(video_link)

            if not video_id:
                messages.warning(request, "Enter only embeded code")
                return redirect('/admin/video_gallery_list')
            form.save()
            messages.success(request, "Video Added Successfully")
        else:
            messages.error(request, "Error Adding Video")
        return redirect('/admin/video_gallery_list')
    else:
        messages.warning(request, "Only POST method is allowed for this operation.")
        return redirect('/admin/video_gallery_list')
 

def delete_video_from_gallery(request,id):
    VideoGallery.objects.get(id=id).delete()
    return redirect("/admin/video_gallery_list")





@login_required
def enquiry_list(request):
    enquiries = Enquiry.objects.order_by('-id')
    return render(request, 'enquiry_list.html', {'enquiries': enquiries})

def delete_enquiry(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("/admin/enquiry_list")





def news_list(request):
    news_form = NewsForm()
    news_data = News.objects.all().order_by("-id")
    context = {
        "news_form": news_form,
        "news_data": news_data,
    }
    return render(request, 'admin_news_list.html', context)

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "News Created Successfully")
            return redirect('/admin/news_list')
        else:
            messages.warning(request, "Error Creating News")
    return redirect('/admin/news_list')

def update_news(request, id):
    news_data = get_object_or_404(News, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_data)
        if form.is_valid():
            form.save()
            messages.success(request, "News Updated Successfully")
        else:
            messages.error(request, "Error Updating News")
            return render(request, 'admin_update_news.html', {'form': form})
    else:
        form = NewsForm(instance=news_data)
    return render(request, 'admin_update_news.html', {'form': form})

def delete_news(request, id):
    News.objects.get(id=id).delete()
    messages.success(request, "News Deleted Successfully")
    return redirect('/admin/news_list')


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    photos_videos = NewsPhotosVideos.objects.filter(news=news) 
 
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
    form = NewsPhotosVideosForm()
 
    return render(request, 'admin_news_details.html', {
        'news': news,
        'photos_videos': photos_videos,
        'form': form,
        'video_data': video_data,
    })


def extract_video_id(embed_url):
    match = re.search(r"embed/([a-zA-Z0-9_-]+)", embed_url)
    if match:
        return match.group(1)
    return None

def create_news_photos_videos(request):
    if request.method == 'POST':
        form = NewsPhotosVideosForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            video_link = form.cleaned_data.get('video_link')
            if video_link:
                video_id=extract_video_id(video_link)
            if not image and not video_link:
                messages.warning(request, "At least one of the fields (image or video) is required.")
                return redirect(f'/admin/news_details/{request.POST.get("news")}')
 
            if video_link:
                video_id=extract_video_id(video_link)
                if not video_id:
                    messages.warning(request, "Enter only embeded code")
                    return redirect(f'/admin/news_details/{request.POST.get("news")}')
                else:
                    form.save()
                    messages.success(request, "Photo/Video Added Successfully")
                    return redirect(f"/admin/news_details/{request.POST.get('news')}")

            form.save()
            messages.success(request, "Photo/Video Added Successfully")
        else:
            messages.error(request, "Error Adding Photo/Video")
        return redirect(f"/admin/news_details/{request.POST.get('news')}")
    else:
        messages.warning(request, "Only POST method is allowed for this operation.")
        return redirect("/admin/news_list")




def delete_news_photos(request,id):
    news_image = NewsPhotosVideos.objects.filter(id=id).first()
    news_id=news_image.news.id
    if news_image.video_link:
       NewsPhotosVideos.objects.filter(id=id).update(image="")
    else:
        news_image.delete()
    return redirect(f"/admin/news_details/{news_id}")


def delete_news_video(request,id):
    news = NewsPhotosVideos.objects.filter(id=id).first()
    news_id=news.news.id
    if news.image:
       NewsPhotosVideos.objects.filter(id=id).update(video_link="")
    else:
        news.delete()
    return redirect(f"/admin/news_details/{news_id}")
