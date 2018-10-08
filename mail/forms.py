from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='문의하시는 분의 연락처')
    message = forms.CharField(widget=forms.Textarea, required=True, label='문의 내용')


class SendBrochureForm(forms.Form):
    receiver_email = forms.EmailField(required=True, label='', widget=forms.TextInput(
        attrs={'type': 'email', 'placeholder': '이메일 주소 입력'}
    ))