from django.shortcuts import render
from .models import Painting, PaintingImg
from mail.forms import ContactForm, SendBrochureForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.utils import translation

# Create your views here.
def allPaintings(request):
    paintings_list = Painting.objects.all().order_by('-date_added')
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
    return render(request, 'shop/paintings.html', {'form': form, 'paintings': paintings})

def paintingDetail(request, painting_slug):
    brochure_form = SendBrochureForm()
    try:
        painting = Painting.objects.get(slug = painting_slug)
        paintingImgs = painting.images.all()
    except Exception as e:
        raise e
    return render(request, 'shop/detail.html', {'painting': painting, 'paintingImgs': paintingImgs, 'brochure_form': brochure_form})