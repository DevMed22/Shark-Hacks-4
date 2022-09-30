from django.views.generic import FormView, ListView, DetailView
from .forms import addQuestionform
from .models import QuesModel
from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        for q in questions:
            print(request.POST.get(q.question))
            # print(q.ans)
            print()
            ans = False
            if str(q.ans) ==  str(request.POST.get(q.question)):
                ans = True
            else:
                break

        context = {
            'ans':ans
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'questions.html',context)