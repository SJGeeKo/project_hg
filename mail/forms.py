from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50, label='이름')
    from_contact = forms.CharField(required=True, label='연락처')
    message = forms.CharField(widget=forms.Textarea, required=True, label='문의내용')

class SendBrochureForm(forms.Form):
    receiver_email = forms.EmailField(required=True, label='', widget=forms.TextInput(
        attrs={'type': 'email', 'placeholder': '이메일 주소 입력'}
    ))