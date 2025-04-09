from django import forms
from .models import Event, Enquiry, Booking, Gallery, ClientReview

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        
        
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'