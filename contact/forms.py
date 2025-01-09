from django.core.exceptions import ValidationError
from .models import Contact 
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone', 'e_mail', 'description', 'category',

    def clean(self):
        cleaned_data = self.cleaned_data

        if 1==0:
            self.add_error(
                'first_name',
                ValidationError(
                    'Error message',
                    code='Invalid'
                )
            )

        return super().clean()

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)