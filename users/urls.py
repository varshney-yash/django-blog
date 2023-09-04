from django.urls import path
from django.views.generic import RedirectView
from .views import register,profile,upload_image


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='register', permanent=False)),
    path('register/', register, name='register'),
    path('profile/',profile,name='profile'),
    path('test-upload',upload_image)
]