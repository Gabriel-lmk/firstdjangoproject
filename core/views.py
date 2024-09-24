from pathlib import Path
from itertools import product
from lib2to3.fixes.fix_input import context
from tempfile import template
from django.templatetags.static import static
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from core.models import Product
from django.template import loader

def index(request):

    products = Product.objects.all()

    context = {
        'curso': 'Salamence do Django',
        'outro': 'Pode ser um Salamence, mas ele ainda tem muito a aprender',
        'products': products
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def product(request, pk):
    #prod = Product.objects.get(id=pk)
    prod = get_object_or_404(Product, id=pk)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)