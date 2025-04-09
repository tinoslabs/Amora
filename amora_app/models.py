from django.db import models

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200, null=True, blank=True)
    team_name = models.CharField(max_length=200, null=True, blank=True)
    event_details = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    event_video = models.FileField(upload_to='event_video/', null=True, blank=True)
    event_image = models.ImageField(upload_to='images/', null=True, blank=True)
    seat_avilability = models.IntegerField(null=True, blank=True)
    venue = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.event_name
    
    
class Enquiry(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True) 
    last_name = models.CharField(max_length=100, blank=True, null=True) 
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.first_name 
    
    
class Booking(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True) 
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    def __str__(self):
        return self.name 
    
    
class Gallery(models.Model):
    event_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
   
    date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.event_name 
    
class ClientReview(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_image = models.ImageField(upload_to='client_images/', null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.client_name} - {self.designation}"
    
    