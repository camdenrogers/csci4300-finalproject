import datetime

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Event, EventGroups, EventRegistered
from events.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

import requests
# Create your views here.

def index(request):
    return render(request, 'events/index.html', {})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url= 'http://172.19.50.172/final/events/'
    template_name = 'registration/signup.html'

# event list response with last 5 questions
class IndexView(generic.ListView):
    template_name = 'events/events.html'
    context_object_name = 'latest_event_list'
    def get_queryset(self):
        """Return the 15 events (not including those set to be
        published in the future). """
        return Event.objects.filter().order_by('id')[:24]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_queryset(self):
        return Event.objects.filter()

def Groups(request, num):
    event = Event.objects.filter(id=num)
    g = EventGroups.objects.filter(event=event[0]).order_by('id')
    users = EventRegistered.objects.filter(event=event[0])
    context = {'event': event[0], 'group_list': g, 'user_list': users}
    return render(request, 'events/groups.html', context)

def NewGroup(request, num):
    e = Event.objects.filter(id=num)
    e = e[0]
    group = EventGroups(event = e)
    group.save()
    g = EventGroups.objects.filter(event=e).order_by('id')
    users = EventRegistered.objects.filter(event=e)
    context = {'event': e, 'group_list': g, 'user_list': users}
    return render(request, 'events/groups.html', context)

def JoinGroup(request, eventnum, groupnum):
    e = Event.objects.filter(id=eventnum)
    g = EventGroups.objects.filter(id=groupnum)
    e = e[0]
    register = EventRegistered(event=e, user=request.user.username, group=g[0])
    register.save()
    k = EventGroups.objects.filter(event=e).order_by('id')
    users = EventRegistered.objects.filter(event=e)
    context = {'event': e, 'group_list': k, 'user_list': users}
    return render(request, 'events/groups.html', context) 

def PartialList(request, num):
    template_name = 'events/partiallist.html'
    latest_event_list = Event.objects.filter().order_by('id')[num*24:num*24+24]
    context = {'latest_event_list': latest_event_list }
    return render(request, template_name, context)

def getData(request):
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?size=200&apikey=pNOMkcfwX5Ka9v48lfsfGzUNTCyE8zaW')
    eventData = response.json()
    #return render(request, 'nvite/data.html', {
    #    'data': eventData["_embedded"]["events"][0]["_embedded"]["venues"][0]["city"]["name"],
    #})


    events_array = eventData["_embedded"]["events"]
    i = 0
    while i < len(events_array):
#        try:
#            d=events_array[i]["description"]
#        except KeyError:
#            d=""
        e = Event(event_title=events_array[i]["name"],
                  date=events_array[i]["dates"]["start"]["localDate"],
                  location=events_array[i]["_embedded"]["venues"][0]["city"]["name"],
                  venue_name=events_array[i]["_embedded"]["venues"][0]["name"],
                  venue_latitude=events_array[i]["_embedded"]["venues"][0]["location"]["latitude"],
                  venue_longitude=events_array[i]["_embedded"]["venues"][0]["location"]["longitude"],
        )
        e.save()
        i += 1
    return HttpResponse("You just populated the database")

def map(request):
    return render(request, 'events/map.html', {})
#    return render(request, 'nvite/map.html',{
#        'latitude:
#})


