from django.urls import path
from calculator import views


urlpatterns = [
path('', views.home_view, name='home'),
path('omlet', views.recipes, name='omlet'),
path('pasta', views.recipes, name='pasta'),
path('buter', views.recipes, name='buter'),

]