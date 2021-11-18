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

        ]

    }
    return render(request, 'test_content.html', context)


