from django.views.generic import FormView, ListView, DetailView
from .forms import addQuestionform
from .models import QuesModel
from django.shortcuts import render
from django.contrib.auth.models import User
from pages.models import Player


def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.all()
        # users=User.objects.all()
        for q in questions:
            print(request.POST.get(q.question))
            # print(q.ans)
            print()
            ans = False
            if str(q.ans) == str(request.POST.get(q.question)):
                ans = True
            else:
                break
        player = Player.objects.filter(pk=request.user.id).exists()
        if player:
            if ans:
                k = Player.objects.get(id=request.user.id)
                q = k.survive
                q += 1
                Player.objects.filter(id=request.user.id).update(survive=q)
            else:
                k = Player.objects.get(id=request.user.id)
                q = k.death
                q += 1
                Player.objects.filter(id=request.user.id).update(death=q)
        else:
            Player.objects.create(user=request.user)
            if ans:
                k = Player.objects.get(id=request.user.id)
                q = k.survive
                q += 1
                Player.objects.filter(id=request.user.id).update(survive=q)
            else:
                k = Player.objects.get(id=request.user.id)
                q = k.death
                q += 1
                Player.objects.filter(id=request.user.id).update(death=q)

        context = {
            'ans': ans,
        }
        return render(request, 'result.html', context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'questions.html', context)
