from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Question
from .forms import QuestionForm


# class QuestionView(View):
#     def get(self, request):
#         questions = Question.objects.all()
#         return render(request, 'employees/employees_list.html', context={'employees': employees})

def question_view(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            new_question.save()
    else:
        question_form = QuestionForm()
    return render(request, 'questions/questions_page.html', context={'questions': questions, 'question_form': question_form})
