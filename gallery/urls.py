from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'effecto'

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('nav/',views.nav,name = 'nav'),
    path('base/',views.base,name = 'base'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)