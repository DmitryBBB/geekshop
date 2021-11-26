import json

from django.core.management.base import BaseCommand
from mainapp.models import Products, ProductCategory


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def hadle(selfself,*args,**options):
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')

        Products.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('name')
            _category = ProductCategory.objects.get(id=category)
            prod['category'] =_category
            new_category = Products(**prod)
            new_category.save()