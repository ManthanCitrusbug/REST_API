# -*- coding: utf-8 -*-

from django import forms

from ..models import OtherCode


# -----------------------------------------------------------------------------
# OtherCode
# -----------------------------------------------------------------------------

class OtherCodeCreationForm(forms.ModelForm):
    """Custom OtherCodeCreationForm"""

    class Meta():
        model = OtherCode
        fields = [
            "code",
            "meaning"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(OtherCodeCreationForm, self).clean()
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


class OtherCodeChangeForm(forms.ModelForm):
    """Custom form to change OtherCode"""

    class Meta():
        model = OtherCode

        fields = [
            "code",
            "meaning"
        ]

    def clean(self):
        cleaned_data = super(OtherCodeChangeForm, self).clean()
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