from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.main, name="main"),
    url(r"^fullinfo/", views.fullinfo, name="fullinfo")
]

"""
for element in Fullinfo.objects.all():
    urlpatterns.append(url(r"^varetype/",
                           views.varetype, name="varetype"))
"""
