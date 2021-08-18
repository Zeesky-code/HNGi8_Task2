from django.urls import path, include
from .views import home, contactView

app_name = 'core'

urlpatterns = [
    path('', home, name= 'home'),
    path('contact/',contactView, name= 'contactView'),
]