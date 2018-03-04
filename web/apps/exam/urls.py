from django.urls import path
from . import views
from .app import APP_NAME

app_name = APP_NAME
urlpatterns = [
    path('', views.index, name='index'),
]
