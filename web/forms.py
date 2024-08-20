from django import forms
from web.models import Contact


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'email', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control mb-3 fst-italic', 
                'placeholder': 'Ingrese su nombre aquí'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control mb-3 fst-italic', 
                'placeholder': 'Ingrese su correo aquí'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control mb-3 fst-italic',
                'rows': 5,
                'placeholder': 'Ingrese su mensaje. Máximo 500 caracteres.'
            }),
        }