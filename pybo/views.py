from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.
def index(request):
    """
    create_date로 역정렬한(-가 inverse) Question의 Objects를 question_list로 만듦
    render는 파이썬 데이터를 HTML로 템플릿에 적용해 반환한다.
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
