from . import views
from django.urls import path

app_name = 'students'

urlpatterns = [
    path('', views.indexView.as_view(), name="students"),
]
