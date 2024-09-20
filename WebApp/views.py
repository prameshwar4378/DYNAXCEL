from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def contact_us(request):
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
    return render(request,"career.html")

def career_apply_job(request):
    return render(request,"career_apply_job.html")

def sustainability(request):
    return render(request,"sustainability.html")

def certificates(request):
    return render(request,"web_certificates.html")

def web_photos_gallary(request):
    return render(request,"web_photos_gallary.html")

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
