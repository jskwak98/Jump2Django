from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    """
    장고의 폼은 forms.Form과 forms.ModelForm 두 가지
    모델 폼은 모델과 연결되어 폼을 저장하며, 모델의 데이터를 저장한다.
    Meta class를 override해서 어떤 모델을 사용하고, 그 모델의 어떤 field를 쓸 것인지 써둔다.
    """
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # Question Form에서 사용할 Question Model의 속성
        """
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        # widgets를 Meta에 추가해 attrs를 통해 bootstrap class를 추가할 수 있다.
        # question_form의 {{ form.as_p }} 자동 렌더링 코드를 바꿔줄 것이라 주석처리.
        """
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        # labels를 등록해 모델의 attribute이름의 표시를 바꾼다.


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }