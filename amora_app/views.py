
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.utils import timezone

from .models import Event, Enquiry, Booking, Gallery, ClientReview
from .forms import EventForm, EnquiryForm,GalleryForm, ClientReviewForm
# Create your views here.

def index(request):
    now = timezone.now()

    # Filter upcoming events only
    upcoming_events = Event.objects.filter(end_date__gt=now).order_by('start_date')
    latest_event = upcoming_events.first()  # Only the next upcoming event
    gallery = Gallery.objects.all()
    clients = ClientReview.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        event_id = request.POST.get('event_id')

        if name and phone and email and event_id:
            selected_event = Event.objects.get(id=event_id)
            Booking.objects.create(
                name=name,
                phone=phone,
                email=email,
                event=selected_event
            )
            return redirect('index')  # Adjust to your URL name

    return render(request, 'index.html', {
        'latest_event': latest_event,
        'event': upcoming_events,  # For dropdown form use
        'gallery': gallery,
        'clients':clients
    })

@csrf_protect
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "There was an error logging in, try again...")
            return redirect('user_login')
    return render(request, 'authenticate/login.html', {'form': True})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('index')


@login_required(login_url='user_login')
def admin_dashboard(request):
    return render(request, 'admin_pages/admin_dashboard.html')

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.http import JsonResponse

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})


@login_required(login_url='user_login')
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page
    else:
        form = EventForm()
    return render(request, 'admin_pages/event_form.html', {'form': form, 'action': 'Add Event'})


@login_required(login_url='user_login')
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect("event_list")  # Redirect to the event list page after updating
    else:
        form = EventForm(instance=event)

    return render(request, "admin_pages/update_event.html", {"form": form, "event": event})


@login_required(login_url='user_login')
def delete_event(request, id):  # This now correctly receives 'id'
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, "Event deleted successfully!")
    return redirect('event_list')



def event_list(request):
    events = Event.objects.all()
    return render(request, 'admin_pages/event_list.html', {'events': events})

def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request,'event_details.html',{'event':event})

@login_required(login_url='user_login')
def add_gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')  # Redirect to the event list page
    else:
        form = EventForm()
    return render(request, 'admin_pages/add_gallery.html', {'form': form})


def gallery_list(request):
    gallery = Gallery.objects.all()
    return render(request, 'admin_pages/gallery_list.html', {'gallery': gallery})


@login_required(login_url='user_login')
def update_gallery(request, id):
    gallery = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = GalleryForm(instance=gallery)
    return render(request, 'admin_pages/update_gallery.html', {'form': form, 'gallery': gallery})


@login_required(login_url='user_login')
def delete_gallery(request, id):
    gallery = get_object_or_404(Gallery, id=id)
    gallery.delete()
    return redirect('gallery_list')

@login_required(login_url='user_login')
def add_client_reviews(request):
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews') 
    else:
        form = ClientReviewForm()

    return render(request, 'admin_pages/add_client_reviews.html', {'form': form})


@login_required(login_url='user_login')
def view_client_reviews(request):
    client_reviews = ClientReview.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_client_reviews.html', {'client_reviews': client_reviews})


@login_required(login_url='user_login')
def update_client_reviews(request, id):
    client_reviews = get_object_or_404(ClientReview, id=id)
    if request.method == 'POST':
        form = ClientReviewForm(request.POST, request.FILES, instance=client_reviews)
        if form.is_valid():
            form.save()
            return redirect('view_client_reviews')
    else:
        form = ClientReviewForm(instance=client_reviews)
    return render(request, 'admin_pages/update_client_reviews.html', {'form': form, 'client_reviews': client_reviews})
 

@login_required(login_url='user_login')
def delete_client_review(request,id):
    client_reviews = ClientReview.objects.get(id=id)
    client_reviews.delete()
    return redirect('view_client_reviews')

def service(request):
    return render(request,'service.html')


def event(request):
    event = Event.objects.all().order_by('-id')
    return render(request, 'event.html',{'event':event})

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Redirect to the list view after submission
    else:
        form = EnquiryForm()
    return render(request, 'contact.html',{'form':form})

def enquiry_list(request):
    enquiries = Enquiry.objects.all().order_by('-id')
    return render(request, 'admin_pages/enquiry_list.html', {'enquiries': enquiries})

def delete_enquiry(request, enquiry_id):
    enquiry = get_object_or_404(Enquiry, id=enquiry_id)
    enquiry.delete()
    return redirect('enquiry_list')


def booking_list(request):
    booking = Booking.objects.all().order_by('-id')
    return render(request, 'admin_pages/booking_list.html', {'booking': booking})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('booking_list')

def gallery(request):  
    gallery = Gallery.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})


def products(request):
    return render(request,'products.html')