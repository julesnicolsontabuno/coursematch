from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.indexView.as_view(), name="index"),
]
