from django.db import models

# Create your models here.
from authapp.models import User
from mainapp.models import Products


class Basket(models.Model):
    objects = None
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Корзина для {self.user.name} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def delete(self, using=None, keep_parents=False,*args,**kwargs):
        super(Basket,self).delete(*args,**kwargs)
        self.product.quantity += self.quantity
        self.save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk:
            self.product.quantity -= self.quantity - self.get_item(int(self.pk))


    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity