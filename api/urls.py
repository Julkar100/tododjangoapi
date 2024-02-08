from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import TodoGetCreate, TodoUpdateDelete

urlpatterns = [
    path('', TodoGetCreate.as_view()),
    path('<int:pk>', TodoUpdateDelete.as_view())
]