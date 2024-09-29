 
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
    path('create_career_application', create_career_application, name="create_career_application"),

    path('career_apply_job/<int:id>', career_apply_job, name="career_apply_job"),
    path('sustainability', sustainability, name="sustainability"),
    path('certificates', certificates, name="web_certificates"),
    path('photos_gallary', web_photos_gallary, name="web_photos_gallary"),

    path('services_stainless_steel', stainless_steel, name="stainless_steel"),
    path('services_ASME_PED_Vessels', services_ASME_PED_Vessels, name="services_ASME_PED_Vessels"),
    path('services_railway_metro', services_railway_metro, name="services_railway_metro"),
    path('services_food_farma', services_food_farma, name="services_food_farma"),
    path('services_psa_based', services_psa_based, name="services_psa_based"),
    path('services_defence_equipements', services_defence_equipements, name="services_defence_equipements"),

    path('services_mining', services_mining, name="services_mining"),
    path('services_paper', services_paper, name="services_paper"),
    path('services_power', services_power, name="services_power"),
    path('services_textiles', services_textiles, name="services_textiles"),


]
