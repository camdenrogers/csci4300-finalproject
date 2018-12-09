import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Event

# Create your views here.

def index(request):
    return render(request, 'events/index.html', {})

# event list response with last 5 questions
class IndexView(generic.ListView):
    template_name = 'events/events.html'
    context_object_name = 'latest_event_list'
    def get_queryset(self):
        """Return the 15 events (not including those set to be
        published in the future). """
        return Event.objects.filter().order_by('id')[:15]

class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_queryset(self):
        return Event.objects.filter()
