from django.contrib import admin
from django.urls import path, include
#include untuk menambahkan settingan url pada app
from . import views #ini untuk membaca lokasi index dan login pada views
#semua yg ada di directory sini akan memasukan views ke sini, tapi harus diberi tanda pada url patterns
from login import views as loginViews #memasukan login views pada url base 
urlpatterns = [
    #path('login/',loginViews.index),#diarahkan ke
    path('main', views.main),
    path('',views.main, name='main'),#diarahkan ke
    #path('index', views.index),#diarahkan ke
    path('login/',include('login.urls')),#diarahkan ke
    path('admin/', admin.site.urls),    
]
