from django.urls import path


from . import views

urlpatterns = [
    path('Get_Started/\w/', views.index, name='index'),
    path('?search=<str:topic>', views.index, name='index'),
    path('<str:topic>/results', views.results, name='results'),
]