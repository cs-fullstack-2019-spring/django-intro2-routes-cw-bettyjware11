from django.urls import path

from . import views

urlpatterns = [

    # path('', views.index, name='index'),
    path('gogetthegood/', views.gogetthegood, name='n2'),
    path('happyhappyjoyjoy/', views.happyhappyjoyjoy, name='n3'),

]
