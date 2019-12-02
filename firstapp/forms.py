from django import forms
from django.utils import timezone


class OrderForm(forms.Form):

    name = forms.CharField()
    last_name = forms.CharField(required = False)
    phone = forms.CharField()
    buying_type = forms.ChoiceField(widget=forms.Select(), choices=([('self', 'Pickup'), ('Delivery', 'Delivery')]))
    date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
    address = forms.CharField(required=False)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    def __str__(self, *args, **kwargs):
        super(OrderForm, self).__str__(*args, **kwargs)
        self.fields['name'].label = 'Name'
        self.fields['last_name'].label = 'Last name'
        self.fields['phone'].label = 'Contact number'
        self.fields['phone'].help_text = 'Please, enter a valid phone number'
        self.fields['buying_type'].label = 'Delivery method'
        self.fields['address'].label = 'Delivery address'
        self.fields['address'].help_text = 'Be sure to indicate your city'
        self.fields['comments'].label = 'Your comments'
        self.fields['date'].label = 'Delivery date'
        self.fields['date'].help_text = 'Delivery is made the next day after placing the order. The manager will contact you in advance'

class SearchForm(forms.Form):
    query = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)