from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='picture/')
    address = models.CharField(max_length=150)


class doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='picture/')
    address = models.CharField(max_length=150)


blog_categories = (('Metal Health', 'Metal Health'),
                   ('Heart Disease', 'Heart Disease'),
                   ('Covid19', 'Covid19'),
                   ('Immunization', 'Immunization'),)

draft = (('True', 'True'),
         ('False', 'False'),)

class Doctorpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=blog_categories,max_length=70)
    summary = models.CharField(max_length=70)
    content = models.TextField()
    draft = models.CharField(choices=draft, max_length=50)