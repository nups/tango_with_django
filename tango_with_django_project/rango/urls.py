from django.conf.urls import url
from rango import views

urlpatterns = [
    url('about/', views.about, name = 'about'),
    url('', views.index, name = 'index'),
]