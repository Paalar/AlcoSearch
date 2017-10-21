# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count
from django.utils.encoding import smart_str, smart_unicode

from django.http import HttpResponse
from .models import Fullinfo
from django.template.response import TemplateResponse
from django.db.models import Q

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main(request):
    varetype = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype")
    vin = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="vin") | Q(varetype__icontains="Vermut") | Q(varetype__icontains="Sherry")
                                                       | Q(varetype__icontains="Madeira")).exclude(Q(varetype__icontains="rennevin") | Q(varetype__icontains="lkoholfri"))
    alkoholfritt = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(varetype__icontains="Alkoholfri")
    ol = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="øl") | Q(varetype__icontains="ale") | Q(varetype__icontains="arley") | Q(varetype__icontains="lager")
                                                       | Q(varetype__icontains="Sider") | Q(varetype__icontains="Klosterstil") | Q(varetype__icontains="Porter") | Q(varetype__icontains="Red")
                                                       | Q(varetype__icontains="Mjød") | Q(varetype__icontains="Spesial") | Q(varetype__icontains="Sake")).exclude(varetype__icontains="fritt")
    brennevin = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="rennevin") | Q(varetype__icontains="vodka") | Q(varetype__icontains="Akevitt") | Q(varetype__icontains="Gin")
                                                       | Q(varetype__icontains="Rom") | Q(varetype__icontains="Likør") | Q(varetype__icontains="Whiskey") | Q(varetype__icontains="Genever") | Q(varetype__icontains="Bitter"))
    champagne = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(varetype__icontains="pagne")
    return render(request, "alcosearch/main.html", {"vin": vin, "alkoholfritt": alkoholfritt, "ol": ol, "champagne": champagne, "brennevin": brennevin, "varetype": varetype})


def info(request):
    varetype = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype")
    vin = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="vin") | Q(varetype__icontains="Vermut") | Q(varetype__icontains="Sherry")
                                                       | Q(varetype__icontains="Madeira")).exclude(Q(varetype__icontains="rennevin") | Q(varetype__icontains="lkoholfri"))
    alkoholfritt = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(varetype__icontains="Alkoholfri")
    ol = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="øl") | Q(varetype__icontains="ale") | Q(varetype__icontains="arley") | Q(varetype__icontains="lager")
                                                       | Q(varetype__icontains="Sider") | Q(varetype__icontains="Klosterstil") | Q(varetype__icontains="Porter") | Q(varetype__icontains="Red")
                                                       | Q(varetype__icontains="Mjød") | Q(varetype__icontains="Spesial") | Q(varetype__icontains="Sake")).exclude(varetype__icontains="fritt")
    brennevin = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(Q(varetype__icontains="rennevin") | Q(varetype__icontains="vodka") | Q(varetype__icontains="Akevitt") | Q(varetype__icontains="Gin")
                                                       | Q(varetype__icontains="Rom") | Q(varetype__icontains="Likør") | Q(varetype__icontains="Whiskey") | Q(varetype__icontains="Genever") | Q(varetype__icontains="Bitter"))
    champagne = Fullinfo.objects.values("varetype").annotate(
        Count("varetype")).order_by("varetype").filter(varetype__icontains="pagne")
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
        elif request.POST.get("Advanced"):
            thelist = request.POST.getlist("Advanced", "".encode("utf-8"))
            output = ""
            for i in range(len(thelist)):
                thelist[i] = "Varetype = " + "'" + \
                    thelist[i].replace(",", "_") + "' OR "
                if i == len(thelist) - 1:
                    print(i)
                    output += thelist[-1].replace("OR", "")
                else:
                    output += thelist[i]
            Apl = Fullinfo.objects.raw(
                "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo where " + output.replace("%", "%%") + " order by Apl limit 200;")
            title = ""
        else:
            return render(request, "alcosearch/main.html", {"vin": vin, "alkoholfritt": alkoholfritt, "ol": ol, "champagne": champagne, "brennevin": brennevin, "varetype": varetype})
        return render(request, "alcosearch/info.html", {"Apl": Apl, "title": title, "varetype": varetype, "vin": vin, "alkoholfritt": alkoholfritt, "ol": ol, "champagne": champagne, "brennevin": brennevin})


def fullinfo(request):
    # varetype = Fullinfo.objects.values("varetype").annotate(
    #    Count("varetype")).order_by("varetype")
    Apl = Fullinfo.objects.raw(
        "select ID, Varenummer, Varenavn, Varetype, (Literpris * (100/Alkohol)) as Apl, Alkohol, Pris, Produktutvalg, Vareurl from Fullinfo order by Apl;")
    # data = Fullinfo.objects.filter(
    #    produktutvalg="Basisutvalget").order_by("literpris")
    return render(request, "alcosearch/fullinfo.html", {"Apl": Apl})
