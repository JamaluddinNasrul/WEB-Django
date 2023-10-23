from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def produk(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())
def kategori(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
# Create your views here.
