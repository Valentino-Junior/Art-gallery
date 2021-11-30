from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('nav/',views.nav,name = 'nav'),
    path('base/',views.base,name = 'base'),

    path('search/', views.search_results, name='search'),
    path('location/', views.image_location, name='location'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)