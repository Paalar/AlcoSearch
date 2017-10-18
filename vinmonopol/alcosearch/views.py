# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count
from django.utils.encoding import smart_str, smart_unicode

from django.http import HttpResponse
from .models import Fullinfo
from django.template.response import TemplateResponse


def main(request):
    varetype = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype")
    return render(request, "alcosearch/main.html", {"varetype": varetype})


def info(request):
    if request.method == "POST":
        varetype = request.POST["Varetype"]
        Apl = Fullinfo.objects.raw(
            "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from FullInfo where Varetype = " + "'" + varetype + "'" + " order by Apl limit 100;")
        title = Apl[0]
        return render(request, "alcosearch/info.html", {"Apl": Apl, "title": title})


def vare(request, button):
    Apl = Fullinfo.objects.raw(
        "select ID, Varenummer, Varenavn," + button + ", (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from FullInfo where Alkohol > 0 order by Apl limit;")


def fullinfo(request):
    varetype = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype")
    Apl = Fullinfo.objects.raw(
        "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from FullInfo where Alkohol > 0 and Produktutvalg='Basisutvalget' order by Apl;")
    # data = Fullinfo.objects.filter(
    #    produktutvalg="Basisutvalget").order_by("literpris")
    return render(request, "alcosearch/fullinfo.html", {"varetype": varetype, "Apl": Apl})
