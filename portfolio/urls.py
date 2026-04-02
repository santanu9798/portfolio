from django.urls import path
from . import views

app_name = 'portfolio'
ALLOWED_HOSTS = ['*']

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact'),
]