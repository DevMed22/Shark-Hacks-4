from django.views.generic import FormView, ListView, DetailView
from .forms import addQuestionform
from .models import QuesModel
from django.shortcuts import render


class Questions(ListView):
    model = QuesModel
    context_object_name = 'qs'
    template_name = 'questions.html'


#class Answer(DetailView):

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'questions.html',context)