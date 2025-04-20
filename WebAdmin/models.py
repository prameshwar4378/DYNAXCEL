from django.db import models
import os

# Create your models here.

class PhotoGalleryCategories(models.Model):
    category_name = models.CharField(max_length=255) 
 
    def __str__(self):
        return f"{self.category_name}"

class PhotoGallery(models.Model):
    category = models.ForeignKey(PhotoGalleryCategories, on_delete=models.CASCADE, related_name='photos')
    caption = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="photo_gallery/")
    is_show_on_home_page = models.BooleanField(null=True)

    def delete(self, *args, **kwargs):
        # Delete the image file from the filesystem
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super(PhotoGallery, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.caption} Image"

class VideoGallery(models.Model): 
    caption = models.CharField(max_length=255, blank=True, null=True)
    video_link = models.CharField(blank=True, null=True, help_text="Enter YouTube video link", max_length=255)
  

 
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
    
class News(models.Model):
    title=models.CharField(max_length=200) 
    content=models.TextField()
    thumbnail = models.ImageField(upload_to="news_thumbnail/",  help_text="Recommended Size 1280 x 720 (landscape)", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date=models.DateField(null=True, auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.title
    
    
class NewsPhotosVideos(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news_photos/", blank=True, null=True)
    video_link = models.CharField(blank=True, null=True, help_text="Enter YouTube video link", max_length=255)
    def __str__(self):
        return f"{self.news.title} Photos and Videos"

    def get_youtube_embed_url(self):
        if self.video_link:
            video_id = self.get_video_id()
            print(video_id)
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    def get_video_id(self):
        if self.video_link:
            return self.video_link.split('v=')[-1]
        return None

    def video_thumbnail(self):
        if self.video_link:
            video_id = self.get_video_id()
            return f"https://img.youtube.com/vi/{video_id}/0.jpg"
        return None

    