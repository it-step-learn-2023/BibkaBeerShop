from django.db import models

# Create your models here.
class Post(models.Model):
    # Props:
    title = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=256, unique=True)
    content = models.TextField(max_length=1024, unique=True)
    author = models.CharField(max_length=100)
    image = models.FileField(upload_to='posts/')
    publish = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.title)
    