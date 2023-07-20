from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('fund/', views.fund, name='fund'),
    path('outreach/', views.outreach, name='outreach'),
]
