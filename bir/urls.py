from django.urls import path
from .views import HomeView, AboutView, ServicesView, GalleryView, ContactView

app_name = 'bir'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('about-us/', AboutView.as_view(), name="about_page"),
    path('services/', ServicesView.as_view(), name="services_page"),
    path('gallery/', GalleryView.as_view(), name='gallery_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
]