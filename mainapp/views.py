from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')

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


