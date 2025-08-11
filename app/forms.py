from django import forms

class BookingForm(forms.Form):
    fullname = forms.CharField(max_length=225)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    secondPhone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    description = forms.FileField()
    details = forms.CharField(widget=forms.Textarea)