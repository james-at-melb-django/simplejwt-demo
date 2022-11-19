from django.urls import include, path

urlpatterns = [
    path("simplejwtdemo/api/", include("simplejwtdemo.urls")),
]
