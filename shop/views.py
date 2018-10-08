from django.shortcuts import render
from .models import Painting
from mail.forms import ContactForm, SendBrochureForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def allPaintings(request):
    paintings_list = Painting.objects.all()
    form = ContactForm()
    brochure_form = SendBrochureForm()
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
    return render(request, 'shop/paintings.html', {'form': form, 'brochure_form': brochure_form, 'paintings': paintings})

def paintingDetail(request, painting_slug):
    try:
        painting = Painting.objects.get(slug = painting_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/detail.html', {'painting': painting})