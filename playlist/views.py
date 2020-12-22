from django.db.models import Q
from django.views.generic.list import ListView
from .models import PlaylistTrack, PlaylistEgorCrid

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'playlist/home.html')

def new(request):
    return render(request, 'playlist/new.html')

def chart(request):
    return render(request, 'playlist/chart.html')

def nastroi(request):
    return render(request, 'playlist/Nastroi.html')

class ChartView(ListView):
    model = PlaylistTrack
    template_name = 'playlist/chart.html'
    context_object_name = 'tracks'

class EgorCridView(ListView):
    model = PlaylistEgorCrid
    template_name = 'playlist/EgorCrid.html'
    context_object_name = 'tracks'


class SearchResultsView(ListView):
    model = PlaylistTrack
    template_name = 'playlist/SearchTrack.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = PlaylistTrack.objects.filter(
            Q(TrackName__icontains=query) | Q(TrackAuthor__icontains=query)
        )
        return object_list