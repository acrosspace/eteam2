from django.urls import path
from cass import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("test/", views.test, name="test"),
    path("test2/<int:n>/", views.test2, name="test2")
]