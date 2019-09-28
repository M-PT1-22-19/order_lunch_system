from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Order(models.Model):
    published = models.DateTimeField(auto_now_add=True,
                                     db_index=True, verbose_name='Дата/Время')
    user = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    name_product = models.ForeignKey('Product', related_name='product', verbose_name='Меню',
                                     null=True, on_delete=models.CASCADE)
    # product = models.TextField(verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Количество', default=1)
    # paid = models.IntegerField(verbose_name='Оплачено')
    # price = models.ForeignKey('Product', related_name='paid', verbose_name='Оплачено', on_delete=models.PROTECT,
    #                           default='name_product.price')
    price = models.IntegerField(verbose_name='Оплачено')
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-published']


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='Цена, BYN')

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Меню'

