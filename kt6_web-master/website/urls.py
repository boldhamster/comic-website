from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('news/', views.news, name = 'news'),
    path('cards/', views.cards, name = 'cards'),
    path('issue1/', views.issue1, name = 'issue1'),
    path('otherimages/', views.otherimages, name = 'otherimages'),
    path('contact/', views.contact, name = 'contact'),
]
