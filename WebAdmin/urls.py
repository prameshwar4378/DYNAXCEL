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

    path('certificate_list', certificate_list, name="certificate_list"),
    path('create_certificate', create_certificate, name="create_certificate"),
    path('delete_certificate/<int:id>', delete_certificate, name="delete_certificate"),

    path('photo_gallery_category_list', photo_gallery_category_list, name="photo_gallery_category_list"), 
    path('create_photo_category_for_gallery', create_photo_category_for_gallery, name="create_photo_category_for_gallery"), 
    path('delete_category/<int:id>', delete_category, name="delete_category"), 

    path('photo_gallery_list', photo_gallery_list, name="photo_gallery_list"), 
    path('create_photo_for_gallery', create_photo_for_gallery, name="create_photo_for_gallery"), 
    path('delete_photo_from_gallery/<int:id>', delete_photo_from_gallery, name="delete_photo_from_gallery"), 
    # video Gallary
    path('video_gallery_list', video_gallery_list, name="video_gallery_list"), 
    path('create_video_for_gallery', create_video_for_gallery, name="create_video_for_gallery"), 
    path('delete_video_from_gallery/<int:id>', delete_video_from_gallery, name="admin_delete_video_from_gallery"), 

    path('enquiry_list', enquiry_list, name="admin_enquiry_list"), 
    path('delete_enquiry/<int:id>', delete_enquiry, name="admin_delete_enquiry"), 

    path('news_list/', news_list, name='admin_news_list'),
    path('create_news/', create_news, name='admin_create_news'),
    path('update_news/<int:id>/', update_news, name='admin_update_news'),
    path('delete_news/<int:id>/', delete_news, name='admin_delete_news'),
    path('create_news_photos_videos/', create_news_photos_videos, name='admin_create_news_photos_videos'),
    path('news_details/<int:id>/', news_details, name='admin_news_details'),
    path('delete_news_photos/<int:id>/', delete_news_photos, name='admin_delete_news_photos'),
    path('delete_news_video/<int:id>/', delete_news_video, name='admin_delete_news_video'),

]
