from django import forms
from Review.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields ='__all__'
        fields = ['title','content','star','keywords']

     