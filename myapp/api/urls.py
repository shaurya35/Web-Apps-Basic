from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoute, name="routes"),
    path('', views.getEvents, name="events"),
    path('<str:userId>/', views.getEventfromUserId, name="eventsFromUser")
]