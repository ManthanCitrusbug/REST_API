# -*- coding: utf-8 -*-

from django import forms

from ..models import TimeSlot

# -----------------------------------------------------------------------------
# TimeSlot
# -----------------------------------------------------------------------------

class TimeSlotCreationForm(forms.ModelForm):
    """Custom TimeSlotCreationForm"""

    class Meta():
        model = TimeSlot
        fields = [
            "time_slot",
            "active"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].required = False


    def clean(self):
        cleaned_data = super(TimeSlotCreationForm, self).clean()
        time_slot = cleaned_data.get("time_slot")

        instance = TimeSlot.objects.filter(time_slot=time_slot).first()
        if instance:
            raise forms.ValidationError(
                "Time slot already exists."
            )

        if not time_slot:
            raise forms.ValidationError(
                "Please add Time slot."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance


class TimeSlotChangeForm(forms.ModelForm):
    """Custom form to change TimeSlotChangeForm"""

    class Meta():
        model = TimeSlot

        fields = [
            "time_slot",
            "active"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time_slot'].required = False

    def clean(self):
        cleaned_data = super(TimeSlotChangeForm, self).clean()
        time_slot = cleaned_data.get("time_slot")

        if TimeSlot.objects.filter(time_slot=time_slot).exclude(pk=self.instance.id).count() > 0:
            raise forms.ValidationError(
                "Time slot already exists."
            )
        if not time_slot:
            raise forms.ValidationError(
                "Please add Time slot."
            )

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance