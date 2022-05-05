from django import forms
from library_admin.models import Book
from .models import Author

class AddAuthorForm(forms.ModelForm):

    book = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.SelectMultiple(attrs={'class' : 'form-control w-50 m-auto'}))

    class Meta:
        model = Author
        fields = ['name', 'description', 'book']
        widgets = {
            'name' : forms.TextInput(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
            'description' : forms.Textarea(
                attrs={'class' : 'form-control w-50 m-auto'}
            ),
        }