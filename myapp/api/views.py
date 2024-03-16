from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event
from .serializers import EventSerializer

from django.http import HttpResponse
from .models import Event 
# Create your views here.

@api_view(['GET','POST'])
def getRoute(request):

    routes = [
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Redirect the user to login page'
        },
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Redirects the user to Register page'
        },
        {
            'Endpoint': '/checkAvailableUserID/',
            'method': 'POST',
            'body': None,
            'description': 'Checks for available username'
        },
        {
            'Endpoint': '/addEvent/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new event'
        },
        {
            'Endpoint': '/like/',
            'method': 'POST',
            'body': None,
            'description': 'Checks likes on the events'
        },
    ]
 
    return Response(routes)


@api_view(['GET'])
def getEvents(request):
    Events = Event.objects.all()
    serializer = EventSerializer(Events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEventfromUserId(request, userId):
    Events = Event.objects.filter(id=userId)
    serializer = EventSerializer(Events, many=True)
    return Response(serializer.data)


