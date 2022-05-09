# -*- coding: utf-8 -*-

from django import forms

from ..models import PurchasedProduct


# -----------------------------------------------------------------------------
# PurchasedProduct
# -----------------------------------------------------------------------------

class PurchasedProductCreationForm(forms.ModelForm):
    """Custom PurchasedProduct"""

    class Meta():
        model = PurchasedProduct
        fields = [
            "product",
            "product_price",
            "quantity",
            "user",
            "total_amount",
            "transaction_detail"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PurchasedProductCreationForm, self).clean()
        product = cleaned_data.get("product")
        product_price = cleaned_data.get("product_price")
        quantity = cleaned_data.get("quantity")
        user = cleaned_data.get("user")
        total_amount = cleaned_data.get("total_amount")
        transaction_detail = cleaned_data.get("transaction_detail")

        if not product :
            raise forms.ValidationError(
                "Please add product."
            )
        if not product_price :
            raise forms.ValidationError(
                "Please add product_price."
            )
        if not quantity :
            raise forms.ValidationError(
                "Please add quantity."
            )
        if not user :
            raise forms.ValidationError(
                "Please add user."
            )
        if not total_amount :
            raise forms.ValidationError(
                "Please add total_amount."
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


class PurchasedProductChangeForm(forms.ModelForm):
    """Custom form to change PurchasedProduct"""

    class Meta():
        model = PurchasedProduct

        fields = [
            "product",
            "product_price",
            "quantity",
            "user",
            "total_amount",
            "transaction_detail"
        ]

    def clean(self):
        cleaned_data = super(PurchasedProductChangeForm, self).clean()
        product = cleaned_data.get("product")
        product_price = cleaned_data.get("product_price")
        quantity = cleaned_data.get("quantity")
        user = cleaned_data.get("user")
        total_amount = cleaned_data.get("total_amount")
        transaction_detail = cleaned_data.get("transaction_detail")

        if not product :
            raise forms.ValidationError(
                "Please add product."
            )
        if not product_price :
            raise forms.ValidationError(
                "Please add product_price."
            )
        if not quantity :
            raise forms.ValidationError(
                "Please add quantity."
            )
        if not user :
            raise forms.ValidationError(
                "Please add user."
            )
        if not total_amount :
            raise forms.ValidationError(
                "Please add total_amount."
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