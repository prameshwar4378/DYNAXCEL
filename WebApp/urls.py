 
from django.urls import path
from WebApp.views import  *
urlpatterns = [
    path('/contact-us', contact_us, name="website_contact_us"),
    path('/about_us', about_us, name="website_about_us"),
<<<<<<< HEAD
    path('/career', career, name="website_career"),
    path('/career_apply_job', career_apply_job, name="career_apply_job"),
    path('/infrastructure', infrastructure, name="website_infra"),
=======
    path('/web_news', web_news, name="web_news"),
>>>>>>> 5fe898765030f8cfdcf04130b51a3745f7f6f3ad
]
