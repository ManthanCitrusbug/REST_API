# -*- coding: utf-8 -*-

from django import forms

from ..models import Service


# -----------------------------------------------------------------------------
# Service
# -----------------------------------------------------------------------------

class ServiceCreationForm(forms.ModelForm):
    """Custom Service"""

    class Meta():
        model = Service
        fields = [
            "service_image",
            "booking_charge",
            "detail",
            "service_category",
            "service_charge",
            "name",
            "related_to",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ServiceCreationForm, self).clean()
        booking_charge = cleaned_data.get("booking_charge")
        detail = cleaned_data.get("detail")
        service_category = cleaned_data.get("service_category")
        service_charge = cleaned_data.get("service_charge")
        name = cleaned_data.get("name")

        if not booking_charge :
            raise forms.ValidationError(
                "Please add booking charge."
            )
        if not detail :
            raise forms.ValidationError(
                "Please add detail."
            )
        if not service_category :
            raise forms.ValidationError(
                "Please add service category."
            )
        if not service_charge :
            raise forms.ValidationError(
                "Please add service charge."
            )
        if not name :
            raise forms.ValidationError(
                "Please add name."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class ServiceChangeForm(forms.ModelForm):
    """Custom form to change Service"""

    class Meta():
        model = Service

        fields = [
            "service_image",
            "booking_charge",
            "detail",
            "service_category",
            "service_charge",
            "name",
            "related_to",
        ]

    def clean(self):
        cleaned_data = super(ServiceChangeForm, self).clean()
        booking_charge = cleaned_data.get("booking_charge")
        detail = cleaned_data.get("detail")
        service_category = cleaned_data.get("service_category")
        service_charge = cleaned_data.get("service_charge")
        name = cleaned_data.get("name")

        if not booking_charge :
            raise forms.ValidationError(
                "Please add booking charge."
            )
        if not detail :
            raise forms.ValidationError(
                "Please add detail."
            )
        if not service_category :
            raise forms.ValidationError(
                "Please add service category."
            )
        if not service_charge :
            raise forms.ValidationError(
                "Please add service charge."
            )
        if not name :
            raise forms.ValidationError(
                "Please add name."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance