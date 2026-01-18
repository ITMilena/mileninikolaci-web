from django.shortcuts import render

def pocetna(request):
    return render(request, 'kolaci/pocetna.html')

def ponuda(request):
    return render(request, 'kolaci/ponuda.html')

def kontakt(request):
    return render(request, 'kolaci/kontakt.html')

