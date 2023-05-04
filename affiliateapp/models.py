from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
from django.utils.text import slugify

import datetime
class Product(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    description = models.TextField(default="This is an awesomeproduct")
    price = models.IntegerField(default=100)
    image = models.ImageField(storage=S3Boto3Storage(), default=None)
    altname = models.CharField(max_length=100, default='image')


    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    image = models.ImageField(storage=S3Boto3Storage(), default="www.google.com")
    altname = models.CharField(max_length=100, default='image')
    blog_url = models.TextField(default='blog-url')
    blog_tab_title = models.CharField(max_length=255, default='title')
    blog_description = models.TextField(default='description')
    blog_keywords = models.TextField(default='description')


    def __str__(self):
        return self.title
        
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(storage=S3Boto3Storage(), default="image-link")
    service_url = models.TextField(default='service-url')
    service_tab_title = models.CharField(max_length=255, default='title')
    service_description = models.TextField(default='description')
    service_keywords = models.TextField(default='keywords')
    
    def __str__(self):
        return self.title
    
class CustomerQuery(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Customer queries"

    def __str__(self):
        return self.name
    