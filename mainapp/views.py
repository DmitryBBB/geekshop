from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Geekshop',
    }
    return render(request, 'mainapp/index.html',context)


def products(request):
    context = {
        'title': 'Geekshop - Покупки',
    }
    return render(request, 'mainapp/products.html',context)

def test(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт',
        'user': 'Dmitry Bykov',
        'products':[
            {'name': 'shorts', 'price':'2000rub'},
            {'name': 'boots', 'price': '2300rub'},
            {'name': 'headers', 'price': '7300rub'},


        ]

    }
    return render(request, 'test_content.html', context)


