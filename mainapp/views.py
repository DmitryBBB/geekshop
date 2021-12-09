import json
import os

from django.views.generic import DetailView

from mainapp.models import Products, ProductCategory

MODULE_DIR = os.path.dirname(__file__)



from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Geekshop',
    }
    return render(request, 'mainapp/index.html',context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'Geekshop - Покупки',

    }
   # context['products'] = json.load(open(file_path, encoding='utf-8'))
    context['products'] = Products.objects.all()
    context['categories'] = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', context)



class ProductDetail(DetailView):

    model = Products
    template_name = 'mainapp/detail.html'


    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['products'] = product
        return context



