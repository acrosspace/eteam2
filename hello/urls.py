from django.urls import path
from hello import views
urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("test/<int:id>/", views.test, name="test"),
]