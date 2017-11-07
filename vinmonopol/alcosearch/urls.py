from django.conf.urls import url
from . import views
from django.http import HttpResponse
from django.views.generic import TemplateView

urlpatterns = [
    url(r"^$", views.main, name="main"),
    url(r"^fullinfo/", views.fullinfo, name="fullinfo"),
    url(r"^info/", views.info, name="info"),
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='/robots.txt',
                                                content_type='text/plain')),
]
