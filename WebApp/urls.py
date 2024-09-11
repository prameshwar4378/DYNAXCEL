 
from django.urls import path
from WebApp.views import  *
urlpatterns = [
    path('/contact-us', contact_us, name="website_contact_us"),
    path('/about_us', about_us, name="website_about_us"),
]
