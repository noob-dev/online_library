from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Romeo and Juliet'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Author's name..."}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Enter a description...'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }