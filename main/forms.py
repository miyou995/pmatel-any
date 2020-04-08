from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required = True, max_length=100)
    email = forms.EmailField(required = True)
    subject = forms.CharField( max_length=100)
    phone = forms.CharField(required = True, max_length=16)
    file = forms.FileField(required=False)
    message = forms.CharField(widget=forms.Textarea, required = True)

