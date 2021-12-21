from baskets.models import Basket

def basket(request):
    print(f'Работа контекстного процессора корзины')
    baskets_list = []

    if request.user.is_authenticated:
        baskets_list = Basket.objects.filter(user=request.user)

    return {
        'basket': baskets_list,
    }
