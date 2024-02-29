from django import forms

from movie_service.models import Movie, Actor, Director


class ActorForm(forms.ModelForm):
    name = forms.CharField(max_length=255)

    class Meta:
        model = Actor
        fields = ["name"]


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"class": "select2", "style": "width: 100%;"}
        ),
        required=False,
    )
    directors = forms.ModelMultipleChoiceField(
        queryset=Director.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"class": "select2", "style": "width: 100%;"}
        ),
        required=False,
    )
    release_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Movie
        fields = ["title", "actors", "directors", "release_date"]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        release_date = cleaned_data.get("release_date")
        directors = cleaned_data.get("directors")
        actors = cleaned_data.get("actors")
        return cleaned_data
