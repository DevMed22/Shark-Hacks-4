from django.urls import path
from .views import HomePage, DrawView , TableView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('draw/', DrawView.as_view(), name='draw'),
    path('table/', TableView.as_view(), name='table'),
]