from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:topic>/results', views.results, name='results'),
    path('blog', views.blog, name='blog'),
    path('blog.html', RedirectView.as_view(url='blog')),
    path('index', views.main, name='main'),
    path('index.html', RedirectView.as_view(url='index')),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio.html', RedirectView.as_view(url='portfolio')),
    path('about', views.about, name='about'),
    path('about.html', RedirectView.as_view(url='about')),
    path('contact', views.contact, name='contact'),
    path('contact.html', RedirectView.as_view(url='contact')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)