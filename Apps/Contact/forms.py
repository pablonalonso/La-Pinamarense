from django import forms

class formulario(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50)
    last_name = forms.CharField(label="Apellido", max_length=50)
    gmail = forms.EmailField(label="Gmail")
    message = forms.CharField(label="Contenido",widget=forms.Textarea)

