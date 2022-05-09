# -*- coding: utf-8 -*-

from django import forms

from ..models import ServiceCategory, CategoryImage

# -----------------------------------------------------------------------------
# AdminKeywords
# -----------------------------------------------------------------------------

class ServiceCategoryCreationForm(forms.ModelForm):
    """Custom ServiceCategoryCreationForm"""

    class Meta():
        model = ServiceCategory
        fields = [
            "category_name",
            "category_description",
            "method_description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].required = False
        self.fields['category_description'].required = False

    def clean(self):
        cleaned_data = super(ServiceCategoryCreationForm, self).clean()
        category_name = cleaned_data.get("category_name")
        category_description = cleaned_data.get("category_description")

        instance = ServiceCategory.objects.filter(category_name__iexact=category_name).first()
        if instance:
            raise forms.ValidationError(
                "Category already exists."
            )

        if not category_name:
            raise forms.ValidationError(
                "Please add category name."
            )

        if not category_description:
            raise forms.ValidationError(
                "Please add category description."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class ServiceCategoryChangeForm(forms.ModelForm):
    """Custom form to change ServiceCategory"""

    class Meta():
        model = ServiceCategory

        fields = [
            "category_name",
            "category_description",
            "method_description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].required = False
        self.fields['category_description'].required = False

    def clean(self):
        cleaned_data = super(ServiceCategoryChangeForm, self).clean()
        category_name = cleaned_data.get("category_name")
        category_description = cleaned_data.get("category_description")

        if ServiceCategory.objects.filter(category_name__iexact=category_name).exclude(pk=self.instance.id).count() > 0:
            raise forms.ValidationError(
                "Category already exists."
            )
        if not category_name:
            raise forms.ValidationError(
                "Please add category name."
            )
        if not category_description:
            raise forms.ValidationError(
                "Please add category description."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance

class CategoryImageCreationForm(forms.ModelForm):
    """Custom form to create CategoryImage"""

    class Meta():
        model = CategoryImage
        fields = [
            "category_image",
            "service_category",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # cleaned_data = super(CategoryImageCreationForm, self).clean()

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance