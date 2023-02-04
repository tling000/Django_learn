from django.db import models

# Create your models here.
class Content(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to="media/")
  body = models.TextField()
  published_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title