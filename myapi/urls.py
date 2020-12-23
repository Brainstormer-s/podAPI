
from django.urls import include, path
from . import views

urlpatterns = [
  # path('help', views.help),
  path('featureded', views.featureded),
  path('comedy', views.comedy),
  path('education', views.education), 
  path('fiction', views.fiction), 
  path('business', views.business), 
  path('music', views.music), 
  path('science', views.science), 
  path('sports', views.sports), 
  path('technology', views.technology),
  # podcast detail 
  path('p/<path:link>', views.info), 
  
]