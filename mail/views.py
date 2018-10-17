from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm, SendBrochureForm
from shop.models import Painting

INFO_MAIL_ADDRESS = 'info@hagley.co.kr'

# Create your views here.
def sendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')

            send_mail(
                '새로운 그림 판매 문의입니다.',
                '{}\n\n문의자 연락처: {}'.format(message,from_email),
                INFO_MAIL_ADDRESS,
                [INFO_MAIL_ADDRESS],
            )
    return redirect('shop:allPaintings')

def sendBrochure(request, painting_slug):
    painting = Painting.objects.get(slug=painting_slug)
    if request.method == 'POST':
        form = SendBrochureForm(request.POST)
        if form.is_valid():
            receiver_email = form.cleaned_data.get('receiver_email')

            send_mail(
                '[Hagley] "{}" 작품의 자세한 정보를 보내드립니다.'.format(painting.name),
                'your painting: {}.\nGet details!'.format(painting.name),
                INFO_MAIL_ADDRESS,
                [receiver_email]
            )
    return redirect('shop:paintingDetail', painting_slug=painting_slug)