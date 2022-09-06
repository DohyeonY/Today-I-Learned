from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label='summary',
        widget=forms.TextInput(
            attrs={
                'class': 'my-summary',
                'placeholder': 'Summary',
                'maxlength' : 20,
            }
        )
    )

    memo = forms.CharField(
        label='memo',
        widget=forms.Textarea(
            attrs={
                'class': 'my-memo',
                'placeholder': 'memo',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )

    class Meta:
        model = Memo
        fields = '__all__'
        # exclude = ('title',)
