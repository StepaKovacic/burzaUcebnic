from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length = 200)


class Offer(models.Model):
    description = models.CharField(max_length=500)
    state = models.IntegerField()   #Kolik z deseti třeba. Mby neni important
    contact_info = models.CharField(max_length=200)
    book = models.ForeignKey(Book,on_delete=models.PROTECT)



