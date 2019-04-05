from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_title',\
                    'question_and_anwers_clarification',\
                    'question_and_anwers_premise',\
                    'question_and_anwers_evidence',\
                    'question_and_anwers_origin',\
                    'question_and_anwers_result',\
                    'question_and_anwers_view',\
                    'question_and_anwers_assumption',\
                    )

        def __init__(self, *args, **kwargs):
            super(QuestionForm, self).__init__(*args, **kwargs)
            self.fields['question_and_anwers_clarification'].required = False
            self.fields['question_and_anwers_premise'].required = False
            self.fields['question_and_anwers_evidence'].required = False
            self.fields['question_and_anwers_origin'].required = False
            self.fields['question_and_anwers_result'].required = False
            self.fields['question_and_anwers_view'].required = False
            self.fields['question_and_anwers_assumption'].required = False
        
        # widgets = {
        #     'question_title': forms.TextInput(attrs={'class': 'textinputclass','required':'false'}),
        #     # 'question_and_anwers_clarification': forms.TextInput(attrs={ 'class': 'textinputclass','blank': 'true','null':'true' }),
        #     'question_and_anwers_premise': forms.TextInput(attrs={'required': 'False'}),
        #     'question_and_anwers_evidence': forms.TextInput(attrs={'required': 'False'}),
        #     'question_and_anwers_origin': forms.TextInput(attrs={'required': 'False'}),
        #     'question_and_anwers_result': forms.TextInput(attrs={'required': 'False'}),
        #     'question_and_anwers_view': forms.TextInput(attrs={'required': 'False'}),
        #     'question_and_anwers_assumption': forms.TextInput(attrs={'required': 'False'}),
        # }