from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('nav/',views.nav,name = 'nav'),
    path('base/',views.base,name = 'base'),

]

