from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.TextField(max_length=250)
    image=models.ImageField(upload_to='pics')
    discription=models.TextField()





    def __str__(self):
        return self.name


class People(models.Model):
    name=models.TextField(max_length=25)
    image=models.ImageField(upload_to='pics')
    discription=models.TextField()

    def __str__(self):
        return self.name

class About_us(models.Model):

    image = models.ImageField(upload_to='pics')



class Footer(models.Model):
    name = models.TextField(max_length=25)
    image = models.ImageField(upload_to='pics')
    discription = models.TextField()







