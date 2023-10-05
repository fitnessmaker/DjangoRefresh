from django.urls import path
from . import views

urlpatterns = [
    
    
    #path("",views.team,name="team"),
    path("",views.villas,name="villas"),
    path("about",views.about,name="about"),
  

]