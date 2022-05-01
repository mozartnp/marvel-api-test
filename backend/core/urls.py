from django.urls import path
from .views import index, personagens

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('personagens/', personagens, name='personagens'),
]