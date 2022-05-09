# -*- coding: utf-8 -*-

from django import forms

from ..models import ShopProduct


# -----------------------------------------------------------------------------
# ShopProduct
# -----------------------------------------------------------------------------

class ShopProductCreationForm(forms.ModelForm):
    """Custom ShopProduct"""

    class Meta():
        model = ShopProduct
        fields = [
            "product_image",
            "name",
            "price",
            "detail"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ShopProductCreationForm, self).clean()
        name = cleaned_data.get("name")
        price = cleaned_data.get("price")
        detail = cleaned_data.get("detail")

        if not name :
            raise forms.ValidationError(
                "Please add name."
            )
        if not price :
            raise forms.ValidationError(
                "Please add price."
            )
        if not detail :
            raise forms.ValidationError(
                "Please add detail."
            )
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class ShopProductChangeForm(forms.ModelForm):
    """Custom form to change ShopProduct"""

    class Meta():
        model = ShopProduct

        fields = [
            "product_image",
            "name",
            "price",
            "detail"
        ]

    def clean(self):
        cleaned_data = super(ShopProductChangeForm, self).clean()
        name = cleaned_data.get("name")
        price = cleaned_data.get("price")
        detail = cleaned_data.get("detail")

        if not name :
            raise forms.ValidationError(
                "Please add name."
            )
        if not price :
            raise forms.ValidationError(
                "Please add price."
            )
        if not detail :
            raise forms.ValidationError(
                "Please add detail."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance