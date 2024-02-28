from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm

def index(request):
    """

    pybo 목록 출력
    """

    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'pybo/question_list.html', context)
    return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")



def detail(request, question_id):
    """
    pybo 내용 출력 
    
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)    


def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    """
    
    pybo 질문등록
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


#! def question_create(request):
#     context = {}
#     ...
#     context["form"]=[form]
#     return render(request, 'pybo/question_form.html', context) 이거 113쪽인데 이런 형태로 하라는건가?
