from django.urls import path
from .views import * 

urlpatterns = [ 
    path('dashboard', dashboard, name="admin_dashboard"), 

    path('career_list/', career_list, name='admin_career_list'),
    path('create_career/', create_career, name='admin_create_career'),
    path('update_career/<int:id>', update_career, name="admin_update_career"), 
    path('delete_career/<int:id>', delete_career, name="admin_delete_career"), 

    path('job_application_list/', job_application_list, name="admin_job_application_list"), 
    path('delete_job_applicattion/<int:id>', delete_job_applicattion, name="admin_delete_job_applicattion"), 

    path('photo_gallery_list', photo_gallery_list, name="photo_gallery_list"), 
    path('create_photo_for_gallery', create_photo_for_gallery, name="create_photo_for_gallery"), 
    path('delete_photo_from_gallery/<int:id>', delete_photo_from_gallery, name="delete_photo_from_gallery"), 
    # video Gallary
    path('video_gallery_list', video_gallery_list, name="video_gallery_list"), 
    path('create_video_for_gallery', create_video_for_gallery, name="create_video_for_gallery"), 
    path('delete_video_from_gallery/<int:id>', delete_video_from_gallery, name="delete_video_from_gallery"), 

    path('enquiry_list', enquiry_list, name="admin_enquiry_list"), 
    path('delete_enquiry/<int:id>', delete_enquiry, name="admin_delete_enquiry"), 

]
