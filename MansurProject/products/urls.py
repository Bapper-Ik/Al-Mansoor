from django.urls import path
from . import views

app_name = 'mansur'
urlpatterns = [
    path('', views.index, name='index'),
    path('atampa', views.atampa, name='atampa'),
    path('gov', views.gov, name='gov'),
    path('plain', views.plain, name='plain'),
    path('osaka', views.osaka, name='osaka'),
    path('tissue', views.tissue, name='tissue'),
    path('cashmere', views.cashmere, name='cashmere'),
    path('staroz', views.staroz, name='staroz'),
    path('lana', views.lana, name='lana'),

    path('getzner', views.getzner, name='getzner'),
    path('nbtx', views.nbtx, name='nbtx'),
    path('shampo', views.shampo, name='shampo'),
    path('water', views.water, name='water'),
    path('wagambari', views.wagambari, name='wagambari'),

    path('men', views.men, name='men'),
    path('women', views.women, name='women'),

    path('about', views.about, name='about'),
    path('trends', views.trends, name='trends'),
    path('contact', views.contact, name='contact'),
    path('comment', views.adding_comment, name='comment')

]
