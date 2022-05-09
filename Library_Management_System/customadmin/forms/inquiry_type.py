# -*- coding: utf-8 -*-

from django import forms

from ..models import InquiryType

# -----------------------------------------------------------------------------
# Inquiry type
# -----------------------------------------------------------------------------

class InquiryTypeCreationForm(forms.ModelForm):
    """Custom InquiryTypeCreationForm"""

    class Meta():
        model = InquiryType
        fields = [
            "inquiry_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inquiry_type'].required = False


    def clean(self):
        cleaned_data = super(InquiryTypeCreationForm, self).clean()
        inquiry_type = cleaned_data.get("inquiry_type")

        instance = InquiryType.objects.filter(inquiry_type__iexact=inquiry_type).first()
        if instance:
            raise forms.ValidationError(
                "Inquiry type already exists."
            )

        if not inquiry_type:
            raise forms.ValidationError(
                "Please add inquiry type."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class InquiryTypeChangeForm(forms.ModelForm):
    """Custom form to change InquiryTypeChangeForm"""

    class Meta():
        model = InquiryType

        fields = [
            "inquiry_type",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inquiry_type'].required = False

    def clean(self):
        cleaned_data = super(InquiryTypeChangeForm, self).clean()
        inquiry_type = cleaned_data.get("inquiry_type")

        if InquiryType.objects.filter(inquiry_type__iexact=inquiry_type).exclude(pk=self.instance.id).count() > 0:
            raise forms.ValidationError(
                "Inquiry type already exists."
            )
        if not inquiry_type:
            raise forms.ValidationError(
                "Please add Inquiry type."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance