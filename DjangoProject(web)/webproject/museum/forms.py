from django import forms
from . models import Exhibit, Review


class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['title', 'typeOfArt', 'receiptDate', 'employee', 'hall', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['stars', 'comment']