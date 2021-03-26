from django import forms
from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact
from django.core.exceptions import ValidationError


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "email", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "What would you like to ask about?"

                }
            )
        }


class PrimesForm(forms.Form):
    number = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("number")

        if number < 1:
            raise ValidationError(
                "Number needs to be greater than 1"
            )


class Primes2Form(forms.Form):
    number2 = forms.IntegerField()
    number3 = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        number2 = cleaned_data.get("number2")
        number3 = cleaned_data.get("number3")

        if number2 >= number3:
            raise ValidationError(
                "Number2 needs to be smaller than number3")
        elif number2 < 1 or number3 < 2:
            raise ValidationError(
                "Number2 needs to be higher than 1 and number3 needs to be greater than 2"
            )
        elif number3 > 10001:
            raise ValidationError(
                "Number3 needs to be smaller than 10001"
            )


class DivisorForm(forms.Form):
    number = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        number = cleaned_data.get("number")

        if number > 10001:
            raise ValidationError(
                "Number needs to be smaller than 10001"
            )
        elif number < 1:
            raise ValidationError(
                "Number needs to be greater than 1"
            )
