 
from django.urls import path
from WebApp.views import  *
urlpatterns = [
    path('contact-us', contact_us, name="website_contact_us"),
    path('about_us', about_us, name="website_about_us"),
    path('career', career, name="website_career"),
    path('career_apply_job', career_apply_job, name="career_apply_job"),
    path('infrastructure', infrastructure, name="website_infra"),
    path('web_news', web_news, name="web_news"),
    path('career', career, name="website_career"),
    path('career_apply_job', career_apply_job, name="career_apply_job"),
    path('sustainability', sustainability, name="sustainability"),
    path('certificates', certificates, name="web_certificates"),
    path('photos_gallary', web_photos_gallary, name="web_photos_gallary"),

]
