from .models import Movie
from django import forms
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput

class MovieForm(forms.ModelForm) :
    genre = forms.ChoiceField(
        widget = forms.Select(),
        choices = ([('comedy','comedy'), ('horor', 'horor'), 
                    ('romance', 'romance')]), 
        required = True,

    )

    poster_url = forms.URLField(
        widget=forms.URLInput(
        attrs={
            'placeholder' : 'Poster_url',
        }
        )
    )
    relese_date = forms.DateField(
        widget=NumberInput(
            attrs={'type': 'date'}
            ))
    
    
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Title'
            }
        )
    )

    audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder' : 'Audience'
            }
        )
    ) 
    score = forms.FloatField(
        widget=forms.NumberInput(
                        attrs={
                'min': 0, 'max': 5, 'step' : 0.5, 
                'placeholder' : 'Score'
                }
            ),
        )
    

    class Meta :
        model = Movie


        fields = '__all__'
        # exclude = ('relese_date',)
