from django.core.exceptions import ValidationError
from .models import Contact 
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone',

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Error message',
                code='Invalid'
            )
        )

        return super().clean()
