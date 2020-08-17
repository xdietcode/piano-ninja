from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rowid>/', views.detail, name='detail'),
]