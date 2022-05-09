# -*- coding: utf-8 -*-

from django import forms

from ..models import Testimonial


# -----------------------------------------------------------------------------
# Testimonials
# -----------------------------------------------------------------------------

class TestimonialCreationForm(forms.ModelForm):
    """Custom TestimonialCreationForm"""

    class Meta():
        model = Testimonial
        fields = [
            "name",
            "logo",
            "testimonial_text",
            "designation",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TestimonialCreationForm, self).clean()
        name = cleaned_data.get("name")
        logo = cleaned_data.get("logo")
        designation = cleaned_data.get("designation")
        testimonial_text = cleaned_data.get("testimonial_text")

        if not name :
            raise forms.ValidationError(
                "Please add name."
            )
        if not logo :
            raise forms.ValidationError(
                "Please add logo image."
            )
        if not designation :
            raise forms.ValidationError(
                "Please add designation."
            )
        if not testimonial_text :
            raise forms.ValidationError(
                "Please add testimonial text."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class TestimonialChangeForm(forms.ModelForm):
    """Custom form to change Testimonials"""

    class Meta():
        model = Testimonial

        fields = [
            "name",
            "logo",
            "testimonial_text",
            "designation",
        ]

    def clean(self):
        cleaned_data = super(TestimonialChangeForm, self).clean()
        name = cleaned_data.get("name")
        logo = cleaned_data.get("logo")
        designation = cleaned_data.get("designation")
        testimonial_text = cleaned_data.get("testimonial_text")

        if not name :
            raise forms.ValidationError(
                "Please add name."
            )
        if not logo :
            raise forms.ValidationError(
                "Please add logo image."
            )
        if not designation :
            raise forms.ValidationError(
                "Please add designation."
            )
        if not testimonial_text :
            raise forms.ValidationError(
                "Please add testimonial text."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance