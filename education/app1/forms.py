from django import forms
from app1.models import parent
from app1.models import contact

class parentform(forms.ModelForm):
    class Meta:
        model=parent
        fields='__all__'

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'