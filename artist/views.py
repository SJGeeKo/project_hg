from django.shortcuts import render
from shop.models import Painter, Painting

# Create your views here.
def artistDetailView(request, artist_slug):
    paintings = Painting.objects.all().filter(painter__slug__exact = artist_slug)
    return render(request, 'artist/detail.html', {'paintings': paintings})