from django.db import models

# Create your models here.

class PhotoGallery(models.Model):
    caption = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photo_gallery/")
    is_show_on_home_page=models.BooleanField(null=True)
    def __str__(self):
        return f"{self.caption} Image"
 
class Career(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    posted_on = models.DateField(auto_now_add=True)
    vacancy = models.IntegerField()
    desired_qualification = models.TextField()
    experience_required = models.TextField()
    career_description = models.TextField()
    roles_responsibility = models.TextField()
    skills_required = models.TextField()
    is_publish=models.BooleanField(default=True)
    def __str__(self):
        return self.title

class CareerApplication(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.name} - {self.career.title}'
    

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"