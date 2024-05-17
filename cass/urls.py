from django.urls import path
from cass import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("test/", views.test, name="test"),
    path("test2/<int:n>/", views.test2, name="test2"),
    path("test3/", views.test3, name="test3_base"),
    path("test3/<str:name>/", views.test3, name="test3_name"),
    
    
    path("test4/", views.test4, name="test4"),
    
    
    
    path("test4/<str:object_type>/", views.test4_type, name="test4_object_type"),
    path("test5/", views.test5, name="test5_base"),
    path("test6/", views.test6, name="test6_base"),

    path("test7/", views.test7, name="test7_base"),
]