from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        max_length=50,
        label='Nombre:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic', 
            'placeholder': 'Ingrese su nombre aqui'})
        )
    email = forms.EmailField(
        required=True,
        max_length=100,
        label='Email:',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3 fst-italic', 
            'placeholder': 'Ingrese su correo aqui'})
        )
    mensaje = forms.CharField(
        required=True,
        max_length=500,
        label='Mensaje:',
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3 fst-italic',
            'rows': 5,
            'placeholder': 'Ingrese su mensaje. Maximo 500 caracteres.'})
        )