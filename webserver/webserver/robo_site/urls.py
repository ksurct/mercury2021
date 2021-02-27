from django.urls import path
from robo_site import views

urlpatterns = [
    path('server/<str:blob>/', views.robo_site, name='robo_site'),
    path('test/', views.test, name='robo_site'),
    path('', views.main, name='robo_site'),
]
