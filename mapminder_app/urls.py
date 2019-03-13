
from django.urls import path
from . import views

app_name = 'mapminder_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('chart/', views.index, name='chart'),
    path('explanation/', views.explanation, name='explanation')
]
