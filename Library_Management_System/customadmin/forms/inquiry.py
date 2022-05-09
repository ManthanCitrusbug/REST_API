# -*- coding: utf-8 -*-

from django import forms

from ..models import Inquiry, InquiryType
# -----------------------------------------------------------------------------
# Plans
# -----------------------------------------------------------------------------
class InquiryCreationForm(forms.ModelForm):
    """Custom InquiryCreationForm."""

    class Meta:
        model = Inquiry
        fields = [
            "name",
            "email",
            "phone",
            "inquiry_type",
            "note"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inquiry_type'].required = False
        self.fields['note'].required = False

    def clean(self):
        cleaned_data = super(InquiryCreationForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        inquiry_type = cleaned_data.get("inquiry_type")

        if not name:
            raise forms.ValidationError(
                "Please enter name."
            )
        if not email:
            raise forms.ValidationError(
                "Please enter email."
            )
        if not phone:
            raise forms.ValidationError(
                "Please enter phone."
            )
        if not inquiry_type:
            raise forms.ValidationError(
                "Please enter inquiry_type."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance



class InquiryChangeForm(forms.ModelForm):
    """Custom InquiryChangeForm."""
    class Meta:
        model = Inquiry
        fields = (
            "name",
            "email",
            "phone",
            "inquiry_type",
            "note"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inquiry_type'].required = False
        self.fields['note'].required = False

    def clean(self):
        cleaned_data = super(InquiryChangeForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone = cleaned_data.get("phone")
        inquiry_type = cleaned_data.get("inquiry_type")

        if not name:
            raise forms.ValidationError(
                "Please enter name."
            )
        if not email:
            raise forms.ValidationError(
                "Please enter email."
            )
        if not phone:
            raise forms.ValidationError(
                "Please enter phone."
            )
        if not inquiry_type:
            raise forms.ValidationError(
                "Please enter inquiry_type."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
