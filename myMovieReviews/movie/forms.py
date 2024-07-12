from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'openingDate', 'genre', 'score', 'runningtime', 'text', 'director', 'actor')