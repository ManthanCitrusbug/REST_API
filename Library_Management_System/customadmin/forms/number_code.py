# -*- coding: utf-8 -*-

from django import forms

from ..models import NumberCode


# -----------------------------------------------------------------------------
# NumberCode
# -----------------------------------------------------------------------------

class NumberCodeCreationForm(forms.ModelForm):
    """Custom NumberCodeCreationForm"""

    class Meta():
        model = NumberCode
        fields = [
            "code",
            "meaning"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(NumberCodeCreationForm, self).clean()
        code = cleaned_data.get("code")
        meaning = cleaned_data.get("meaning")

        if not code :
            raise forms.ValidationError(
                "Please add code."
            )
        if not meaning :
            raise forms.ValidationError(
                "Please add meaning."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class NumberCodeChangeForm(forms.ModelForm):
    """Custom form to change NumberCode"""

    class Meta():
        model = NumberCode

        fields = [
            "code",
            "meaning"
        ]

    def clean(self):
        cleaned_data = super(NumberCodeChangeForm, self).clean()
        code = cleaned_data.get("code")
        meaning = cleaned_data.get("meaning")

        if not code :
            raise forms.ValidationError(
                "Please add code."
            )
        if not meaning :
            raise forms.ValidationError(
                "Please add meaning."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance