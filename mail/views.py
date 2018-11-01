from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm, SendBrochureForm
from shop.models import Painting
from django.http import JsonResponse

INFO_MAIL_ADDRESS = 'info@hagley.co.kr'

# Create your views here.
def sendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            from_contact = form.cleaned_data.get('from_contact')
            message = form.cleaned_data.get('message')

            data = {
                "name": name,
                "from_contact": from_contact,
                "message": message,
            }
            send_mail(
                '새로운 그림 판매 문의입니다.',
                '{}\n\n문의자 이름:{}\n\n문의자 연락처: {}'.format(message, name, from_contact),
                INFO_MAIL_ADDRESS,
                [INFO_MAIL_ADDRESS],
            )
    return JsonResponse(data)

def sendBrochure(request, painting_slug):
    painting = Painting.objects.get(slug=painting_slug)
    if request.method == 'POST':
        form = SendBrochureForm(request.POST)
        if form.is_valid():
            receiver_email = form.cleaned_data.get('receiver_email')

            # send_mail(
            #     '[Hagley] "{}" 작품의 자세한 정보를 보내드립니다.'.format(painting.name),
            #     'your painting: {}.\nGet details!'.format(painting.name),
            #     INFO_MAIL_ADDRESS,
            #     [receiver_email]
            # )
            data = {
                "receiver_email": receiver_email,
                "is_sent": True,
            }
    return JsonResponse(data)