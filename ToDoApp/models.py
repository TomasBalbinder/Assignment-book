from django.db import models
from django.contrib.auth.models import User
from random import choice
from PIL import Image
from django.utils import timezone


# Create your models here.

class TodoModel(models.Model):

    def colour_choices():

        colours = ["#9EDE90",
                    "#DE9B92",
                    "#BC91F2",
                    "#A1ECFF",
                   ]
        colour_choices = choice(colours)
        return colour_choices

    title = models.CharField(max_length=35)
    memo = models.TextField( blank=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_background_colour = models.CharField(max_length=7, default=colour_choices)


    def datetime_field_formatted(self):
        return self.created.strftime("%d.%m.%Y %H:%M")



    def __str__(self):
     
        return f"{self.user.id} {self.user.username} {self.title} {self.datetime_field_formatted()} {self.article_background_colour}" 

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=choice(['profile-p1.png', 
    'profile-p2.png',
    'profile-p3.png', 
    'profile-p4.png', 
    'profile-p5.png', 
    'profile-p6.png', 
    'profile-p7.png', 
    'profile-p8.png' ]), 
    upload_to='profile_pics')

    def __str__(self):
        return f' {self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)





