from django.urls import  path
from .import views

urlpatterns = [
    
    path('index/',views.index,name="index"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="Contact"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login,name="Login")
    
]