from django.urls import path


from . import views

urlpatterns = [
    path('<str:topic>/', views.index, name='index'),
    path('<str:topic>/results', views.results, name='results')
]