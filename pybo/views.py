from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question
from .forms import QuestionForm, AnswerForm


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


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question=question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    """
    from .models import Answer
    
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    """
    # return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    """
    GET이면 question form을 views.question_form과 연결해 render해서 보여주고
    POST면 form을 request.POST에 들어간 값을 넣어서 생성하고, valid check 후,
    question에 저장 후 timedate넣어준 뒤 save한다.
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
