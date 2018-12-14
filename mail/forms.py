from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, label=_('Your name'))
    from_contact = forms.CharField(required=True, label=_('Your email address'))
    message = forms.CharField(widget=forms.Textarea, required=True, label=_('Please provide details of your inquiry below'))

class SendBrochureForm(forms.Form):
    receiver_email = forms.EmailField(required=True, label='', widget=forms.TextInput(
        attrs={'type': 'email', 'placeholder': _('Email')}
    ))