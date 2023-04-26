from django import forms
from .models import Question, Comment



class QuestionForm(forms.ModelForm):
    issue_a = forms.CharField(label="RED TEAM")
    issue_b = forms.CharField(label="BLUE TEAM")
    

    class Meta:
        model = Question
        fields = '__all__'



class CommentForm(forms.ModelForm):

    pick = forms.ChoiceField(
        widget = forms.Select(),
        choices=([(1, 'RED TEAM'), (0, 'BLUE TEAM')]), 
                initial='3', required = True,)

    questions = Question.objects.values('pk')
    pklist = []
    for value in questions :
        pklist.append(value['pk'])
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude=('question_id',)

