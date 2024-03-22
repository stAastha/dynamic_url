# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('home', home, name='home'),
    # path('integer/<int:pk>', integer, name='integer'),
    # path('string/<str:pk>', string, name='string'),
    # path('slug123/<slug:pk>', slug123, name='slug123'),
    # path('path123/<path:pk>', path123, name='path123'), #http://127.0.0.1:8000/app/path123/123sffdd
    path('combination/<path:pk>/<str:id>/<slug:pkid>/<int:idpk>',combination, name='combination')
]

