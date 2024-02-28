from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["title", "release_date", "director", "actors"]

        director = forms.CharField(max_length=255)
        actors = forms.CharField(max_length=255)
        release_date = forms.DateField(
            widget=forms.DateInput(attrs={"type": "date"})
        )
