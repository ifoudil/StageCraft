from django.urls import path
from applistagecraft import views

urlpatterns = [
    path('test/', views.test),
]