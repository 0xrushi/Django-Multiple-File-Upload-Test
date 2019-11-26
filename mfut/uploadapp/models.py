from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Image(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='blog_image')
    image = models.FileField(upload_to='image/')