import os

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView

from mainapp.models import Products, ProductCategory

from django.conf import settings
from django.core.cache import cache

MODULE_DIR = os.path.dirname(__file__)

from django.shortcuts import render


def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = ProductCategory.objects.all()
            cache.set(key,link_category)
        return link_category
    else:
        return ProductCategory.objects.all()


def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Products.objects.all()
            cache.set(key,link_product)
        return link_product
    else:
        return Products.objects.all().select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Products.objects.get(id=pk)
            cache.set(key,product)
        return product
    else:
        return Products.objects.get(id=pk)
# Create your views here.
def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


# @cache_page(3600)
# @never_cache
def products(request, id_category=None, page=1):
    context = {
        'title': 'Geekshop - Покупки',

    }

    if id_category:
        products = Products.objects.filter(category_id=id_category)
    else:
        products = Products.objects.all()

    products = get_link_product()

    paginator = Paginator(products, per_page=3)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context['products'] = products_paginator
    # context['categories'] = ProductCategory.objects.all()
    context['categories'] = get_link_category()
    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Products
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['products'] = get_product(self.kwargs.get('pk'))


        return context
