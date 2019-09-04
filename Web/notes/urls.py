from django.urls import path


from . import views

urlpatterns = [
    path('<int:id>/', views.index, name='index'),
    path('<int:id>/results', views.results, name='results')
]