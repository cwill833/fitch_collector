from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fintch/', views.fintch_index, name='index'),
    path('fintch/<int:fintch_id>/', views.fintch_detail, name='detail'),
    path('fintch/create/', views.FintchCreate.as_view(), name='fintch_create')

]
