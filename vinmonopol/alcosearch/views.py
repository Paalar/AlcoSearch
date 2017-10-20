# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count
from django.utils.encoding import smart_str, smart_unicode

from django.http import HttpResponse
from .models import Fullinfo
from django.template.response import TemplateResponse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main(request):
    varetype = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype")
    return render(request, "alcosearch/main.html", {"varetype": varetype})


def info(request):
    if request.method == "POST":
        if request.POST.get("Varetype"):
            varetype = request.POST["Varetype"].replace(",", "_")
            Apl = Fullinfo.objects.raw(
                "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo where Varetype = " + "'" + varetype.replace("%", "%%") + "'" + " order by Apl limit 200;")
            title = Apl[0]
        elif request.POST.get("Search"):
            search = request.POST["Search"].replace(",", "_")
            Apl = Fullinfo.objects.raw(
                "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo where Varenavn like " + "'%%" + search + "%%'" + " or Varetype like " + "'%%" + search + "%%'" + " order by Apl limit 200;")
            title = request.POST["Search"]
        elif request.POST.get("Top200"):
            Apl = Fullinfo.objects.raw(
                "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo where Alkohol > 0 order by Apl limit 200;")
            title = "Top 200"
    return render(request, "alcosearch/info.html", {"Apl": Apl, "title": title})


def search(request):
    if request.method == "POST":
        search = request.POST["Search"]
        print(search)
        Apl = Fullinfo.objects.raw(
            "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo where Varenavn like " + "'%%" + search + "%%'" + " or Varetype like " + "'%%" + search + "%%'" + " order by Apl limit 200;")
        return render(request, "alcosearch/search.html", {"Apl": Apl})


def fullinfo(request):
    # varetype = Fullinfo.objects.values("varetype").annotate(
    #    Count("varetype")).order_by("varetype")
    Apl = Fullinfo.objects.raw(
        "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo order by Apl;")
    # data = Fullinfo.objects.filter(
    #    produktutvalg="Basisutvalget").order_by("literpris")
    return render(request, "alcosearch/fullinfo.html", {"Apl": Apl})
