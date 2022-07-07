from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.CharField(max_length=10)
    yards = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Shoes(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    size = models.IntegerField()
    male = models.BooleanField()
    status = models.CharField(max_length=10)
    image_url = models.CharField(max_length=2083)


class Atampa(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    cotton = models.BooleanField()
    status = models.CharField(max_length=10)
    image_url = models.CharField(max_length=2083)


class Comments(models.Model):
    customer_email = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_subject = models.CharField(max_length=255)
    customer_message = models.TextField(max_length=1000)


