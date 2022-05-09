# -*- coding: utf-8 -*-

from django import forms

from ..models import PhoneNumberCode


# -----------------------------------------------------------------------------
# PhoneNumberCode
# -----------------------------------------------------------------------------

class PhoneNumberCodeForm(forms.ModelForm):
    """Custom PhoneNumberCode"""

    class Meta():
        model = PhoneNumberCode
        fields = [
            "code",
            "code_text",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PhoneNumberCodeForm, self).clean()
        code = cleaned_data.get("code")
        code_text = cleaned_data.get("code_text")

        if not code :
            raise forms.ValidationError(
                "Please add code."
            )
        if not code_text :
            raise forms.ValidationError(
                "Please add code text."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class PhoneNumberCodeChangeForm(forms.ModelForm):
    """Custom form to change PhoneNumberCode"""

    class Meta():
        model = PhoneNumberCode

        fields = [
            "code",
            "code_text",
        ]

    def clean(self):
        cleaned_data = super(PhoneNumberCodeChangeForm, self).clean()
        code = cleaned_data.get("code")
        code_text = cleaned_data.get("code_text")

        if not code :
            raise forms.ValidationError(
                "Please code."
            )
        if not code_text :
            raise forms.ValidationError(
                "Please add code text."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance