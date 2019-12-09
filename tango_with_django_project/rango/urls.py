from django.conf.urls import url
from django.urls import path, re_path
from rango import views

urlpatterns = [
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url('category/category_name_slug/', views.show_category, name='show_category'),
    url(r'^about/$', views.about, name = 'about'),
    url('add_category/', views.add_category, name='add_category'),
    #url('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    url('', views.index, name = 'index'),

]