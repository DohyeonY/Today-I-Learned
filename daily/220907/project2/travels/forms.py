from django import forms
from .models import Travel


class TravelForm(forms.ModelForm):
    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(
            attrs={
                'class': 'my-location',
                'placeholder': 'ex) 제주도',
                'maxlength': 10,
            }
        )
    )

    plan = forms.CharField(
        label='plan',
        widget=forms.Textarea(
            attrs={
                'class': 'my-plan',
                'placeholder': 'ex) 슉.슈슉.슉',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )
    start_date = forms.DateField(
        label='start date',
        widget=forms.TextInput(
            attrs={
                'class': 'my-start_date',
                'placeholder': 'ex) 2022-02-22',

            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )
    end_date = forms.DateField(
        label='end date',
        widget=forms.TextInput(
            attrs={
                'class': 'my-end_date',
                'placeholder': 'ex) 2022-02-22',

            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )
    class Meta:
        model = Travel
        fields = '__all__'
        # exclude = ('title',)
