
from django.urls import path

from . import views

app_name ='travelapp'

urlpatterns = [

    path('',views.home,name='home'),
    path('details/<int:place_id>/', views.details, name='details'),

]