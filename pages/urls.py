from django.urls import path
from .views import HomePage, DrawView  , Scoreboard

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('draw/', DrawView.as_view(), name='draw'),
    path('table/', Scoreboard.as_view(), name='table'),
]