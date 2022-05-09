# -*- coding: utf-8 -*-

from django import forms

from ..models import BookedService


# -----------------------------------------------------------------------------
# BookedService
# -----------------------------------------------------------------------------

class BookedServiceCreationForm(forms.ModelForm):
    """Custom BookedService"""

    class Meta():
        model = BookedService
        fields = [
            "service",
            "booking_charge",
            "user",
            "service_date",
            "service_time",
            "transaction_detail"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(BookedServiceCreationForm, self).clean()
        service = cleaned_data.get("service")
        booking_charge = cleaned_data.get("booking_charge")
        service_date = cleaned_data.get("service_date")
        service_time = cleaned_data.get("service_time")
        user = cleaned_data.get("user")
        transaction_detail = cleaned_data.get("transaction_detail")

        if not service :
            raise forms.ValidationError(
                "Please add service."
            )
        if not booking_charge :
            raise forms.ValidationError(
                "Please add Booking charge."
            )
        if not service_date :
            raise forms.ValidationError(
                "Please add service date."
            )
        if not user :
            raise forms.ValidationError(
                "Please add user."
            )
        if not service_time :
            raise forms.ValidationError(
                "Please add Service time."
            )
        if not transaction_detail :
            raise forms.ValidationError(
                "Please add transaction_detail."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class BookedServiceChangeForm(forms.ModelForm):
    """Custom form to change BookedService"""

    class Meta():
        model = BookedService

        fields = [
            "service",
            "booking_charge",
            "user",
            "service_date",
            "service_time",
            "transaction_detail"
        ]

    def clean(self):
        cleaned_data = super(BookedServiceChangeForm, self).clean()
        service = cleaned_data.get("service")
        booking_charge = cleaned_data.get("booking_charge")
        service_date = cleaned_data.get("service_date")
        service_time = cleaned_data.get("service_time")
        user = cleaned_data.get("user")
        transaction_detail = cleaned_data.get("transaction_detail")

        if not service :
            raise forms.ValidationError(
                "Please add service."
            )
        if not booking_charge :
            raise forms.ValidationError(
                "Please add Booking charge."
            )
        if not service_date :
            raise forms.ValidationError(
                "Please add service date."
            )
        if not user :
            raise forms.ValidationError(
                "Please add user."
            )
        if not service_time :
            raise forms.ValidationError(
                "Please add Service time."
            )
        if not transaction_detail :
            raise forms.ValidationError(
                "Please add transaction_detail."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance