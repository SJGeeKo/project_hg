from django.shortcuts import render
from shop.models import Painting
from django.db.models import Q
from mail.forms import ContactForm, SendBrochureForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def searchResult(request):
    form = ContactForm()
    brochure_form = SendBrochureForm()
    paintings_list = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        paintings_list = Painting.objects.all().filter(Q(name__contains=query) | Q(description__contains=query) | Q(painter__name__contains=query) | 
        Q(paintingeng__name__contains=query) | Q(paintingeng__description__contains=query) | Q(painter__paintereng__name__contains=query))
    if 'csrfmiddlewaretoken' in request.GET:
        csrfToken = str(request.GET.get('csrfmiddlewaretoken'))
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
    return render(request, 'search/search.html', {'query': query, 'csrfToken': csrfToken, 'paintings':paintings, 'form': form, 'brochure_form': brochure_form})