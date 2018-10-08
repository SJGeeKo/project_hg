from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm, SendBrochureForm

# Create your views here.
def sendEmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data.get('from_email')
            message = form.cleaned_data.get('message')

            send_mail(
                '테스트 제목',
                message,
                from_email,
                ['sungjungeeko@gmail.com'],
            )
    return redirect('shop:allPaintings')

def sendBrochure(request, painting_id):
    if request.method == 'POST':
        form = SendBrochureForm(request.POST)
        if form.is_valid():
            receiver_email = form.cleaned_data.get('receiver_email')

            send_mail(
                'test purchase detail',
                'your painting: {}.\nGet details!'.format(painting_id),
                'sungjungeeko@gmail.com',
                [receiver_email]
            )
    return redirect('shop:allPaintings')