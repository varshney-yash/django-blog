from django.urls import path
from django.views.generic import RedirectView
from .views import register


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='register', permanent=False)),
    path('register/', register, name='register'),
]