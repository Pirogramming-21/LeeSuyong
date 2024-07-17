from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
    path('<int:pk>/increase_interest/', increase_interest, name='increase_interest'),
    path('<int:pk>/decrease_interest/', decrease_interest, name='decrease_interest'),
]