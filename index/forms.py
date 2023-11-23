from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name',
                'id': 'name'
                }
        )
    )

    email = forms.EmailField(required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email',
                'id': 'email'
                }
        )
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Phone',
                'id': 'phone'
                }
        )
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Message',
                'rows': '5'
                }
        )
    )
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']