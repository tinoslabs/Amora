from django.urls import path
from . import views
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('', views.index,name='index'),
    # path('login', views.login, name='login'),
    # path('enquiry', views.enquiry, name='enquiry'),
    path('user_login', views.user_login, name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    
    path('event_list', views.event_list, name='event_list'),
    path('add_event', views.add_event, name='add_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:id>/', views.delete_event, name='delete_event'),
  
    path('events/<int:event_id>/', views.event_details, name='event_details'), 
    path('event', views.event , name='event'),
    path('enquiry_list', views.enquiry_list, name='enquiry_list'),
    path('enquiries/delete/<int:enquiry_id>/', views.delete_enquiry, name='delete_enquiry'),
    
    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),    
    path('service',views.service,name='service'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('products',views.products,name='products'),
    
    
    path('booking_list', views.booking_list, name='booking_list'),
    path('delete_booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    
    path('add_gallery', views.add_gallery, name='add_gallery'),
    path('gallery_list', views.gallery_list, name='gallery_list'),
    path('update-gallery/<int:id>/', views.update_gallery, name='update_gallery'),
    path('delete_gallery/<int:id>/', views.delete_gallery, name='delete_gallery'),
    
    path('add_client_reviews',views.add_client_reviews,name='add_client_reviews'),
    path('view_client_reviews',views.view_client_reviews,name='view_client_reviews'),
    path('update_client_reviews/<int:id>/',views.update_client_reviews,name='update_client_reviews'),
    path('delete_client_review/<int:id>/',views.delete_client_review,name='delete_client_review'),
]