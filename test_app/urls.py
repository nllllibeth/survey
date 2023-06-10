from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/<str:login>/', views.create, name='create'),
    path('test/<str:id>/<str:login>/', views.vote, name='vote'),
    path('results/<str:id>/<str:login>/', views.get_results, name='results'),
    path('results_page/', views.get_results_page, name='results_page'),
    path('scores/', views.get_scores, name='get_scores'),
]