from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guest/', views.guest_list, name='guest_list'),
    path('guest/new/', views.new_guest, name='new_guest'),
    path('guest/<int:pk>/edit/', views.update_guest, name='update_guest'),
    path('intake/', views.intake_list, name='intake_list'),
    path('intake/new/', views.new_intake, name='new_intake'),
    path('intake/<int:pk>/edit/', views.update_intake, name='update_intake'),
    path('turnaway/', views.turnaway_list, name='turnaway_list'),
    path('turnaway/new/', views.new_turnaway, name='new_turnaway'),
    path('turnaway/<int:pk>/edit/', views.update_turnaway, name='update_turnaway'),
    path('statistics/', views.Statistics, name='statistics'),
]