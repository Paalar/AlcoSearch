from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.main, name="main"),
    url(r"^fullinfo/", views.fullinfo, name="fullinfo"),
    url(r"^info/", views.info, name="info"),
    url(r"^search/", views.search, name="search")
]
