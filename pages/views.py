from django.views.generic import TemplateView, ListView
from .models import Player

class HomePage(TemplateView):
    template_name = 'index.html'


class DrawView(TemplateView):
    template_name = 'draw.html'


#class TableView(TemplateView):
 #   template_name = 'table.html'


class Scoreboard(ListView):
    model=Player
    template_name='table.html'
    context_object_name='players'