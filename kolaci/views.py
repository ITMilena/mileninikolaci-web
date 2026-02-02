from django.shortcuts import render


def home(request):
    return render(request, "kolaci/home.html")


def ponuda(request):
    return render(request, "kolaci/ponuda.html")


def kontakt(request):
    return render(request, "kolaci/kontakt.html")


def onama(request):
    return render(request, "kolaci/onama.html")


def cenovnik(request):
    return render(request, "kolaci/cenovnik.html")
