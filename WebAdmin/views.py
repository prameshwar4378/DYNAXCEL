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
    return render(request,"admin_dashboard.html")
 
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



@login_required
def video_gallery_list(request): 
    data = VideoGallery.objects.all()
    form = VideoGalleryForm()
    return render(request, 'admin_video_gallary_list.html', {'form': form, "data":data})


def create_video_for_gallery(request):
    if request.method == 'POST':
        form = VideoGalleryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"Video Added Success")
            return redirect('/admin/video_gallery_list') 
        else:
            messages.error(request,"Form is not valid")
            return redirect('/admin/video_gallery_list') 
             # Assuming you have a URL named 'list' for listing events
    else: 
            messages.error(request,"Invalid request method")
            return redirect('/admin/video_gallery_list')  # Assuming you have a URL named 'list' for listing events

 
def delete_video_from_gallery(request, id):
    # Get the video object or return a 404 error if not found
    video = get_object_or_404(VideoGallery, id=id)

    # Check if the video file exists and delete it
    if video.video:
        video.video.delete(save=False)  # This deletes the file from the filesystem

    # Now delete the video object from the database
    video.delete()

    # Redirect to the video gallery list
    return redirect("/admin/video_gallery_list")


@login_required
def enquiry_list(request):
    enquiries = Enquiry.objects.order_by('-id')
    return render(request, 'enquiry_list.html', {'enquiries': enquiries})

def delete_enquiry(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("/admin/enquiry_list")

