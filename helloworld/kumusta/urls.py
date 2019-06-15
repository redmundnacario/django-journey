from django.urls import path
from . import views

urlpatterns = [
    path('kumusta', views.viewKumustaPage, name='kumusta'),
]