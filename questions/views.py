from django.views.generic import FormView, ListView, DetailView
from .forms import addQuestionform
from .models import QuesModel

class Questions(ListView):
    model = QuesModel
    context_object_name = 'qs'
    template_name = 'questions.html'


class Answer(DetailView):
    