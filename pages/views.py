from django.views.generic import TemplateView, ListView


class HomePage(TemplateView):
    template_name = 'index.html'


class DrawView(TemplateView):
    template_name = 'draw.html'


class TableView(TemplateView):
    template_name = 'table.html'
