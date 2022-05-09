# -*- coding: utf-8 -*-

from django import forms

from ..models import CategoryImage


# -----------------------------------------------------------------------------
# CategoryImage
# -----------------------------------------------------------------------------

class CategoryImageCreationForm(forms.ModelForm):
    """Custom CategoryImageCreationForm"""

    class Meta():
        model = CategoryImage
        fields = [
            "category_image",
            "service_category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryImageCreationForm, self).clean()
        category_image = cleaned_data.get("category_image")
        service_category = cleaned_data.get("service_category")

        if not category_image :
            raise forms.ValidationError(
                "Please add category image."
            )
        if not service_category :
            raise forms.ValidationError(
                "Please add service category."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)
        cleaned_data = super(CategoryImageCreationForm, self).clean()

        if commit:
            instance.save()

        return instance


class CategoryImageChangeForm(forms.ModelForm):
    """Custom form to change CategoryImage"""

    class Meta():
        model = CategoryImage

        fields = [
            "category_image",
            "service_category",
        ]

    def clean(self):
        cleaned_data = super(CategoryImageChangeForm, self).clean()
        category_image = cleaned_data.get("category_image")
        service_category = cleaned_data.get("service_category")

        if not category_image :
            raise forms.ValidationError(
                "Please add category image."
            )
        if not service_category :
            raise forms.ValidationError(
                "Please service category."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance