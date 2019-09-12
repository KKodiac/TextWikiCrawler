from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('Get_Started/', views.index, name='index'),
    path('?search=<str:topic>', views.index, name='index'),
    path('', views.main, name='main'),
    path('<str:topic>/results', views.results, name='results'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)