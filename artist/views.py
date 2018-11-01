from django.shortcuts import render
from shop.models import Painter, Painting
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from mail.forms import ContactForm

# Create your views here.
def artistDetailView(request, artist_slug):
    paintings_list = Painting.objects.all().filter(painter__slug__exact = artist_slug)
    form = ContactForm()
    '''
    Paginator
    '''
    paginator = Paginator(paintings_list, 16)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        paintings = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paintings = paginator.page(paginator.num_pages)
    return render(request, 'artist/detail.html', {'paintings': paintings, 'form': form})