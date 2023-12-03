from django import forms
from .models import Book,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= [
            'name',
        ]
        Widgets={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_of_book',
            'photo_of_author',
            'pages_number',
            'price',
            'rental_per_day_price',
            'rental_period',
            'Toatal_rental',
            'status',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_of_book': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_of_author': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pages_number': forms.NumberInput(attrs={'class': 'form-control'}),  # Use NumberInput for IntegerField
            'price': forms.NumberInput(attrs={'class': 'form-control'}), 
            'rental_per_day_price': forms.NumberInput(attrs={'class': 'form-control','id':'rental_price_per_day'}),  
            'rental_period': forms.NumberInput(attrs={'class': 'form-control','id':'rental_period'}), 
            'Toatal_rental': forms.NumberInput(attrs={'class': 'form-control','id':'Toatal_rental_price'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
