from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class Order(models.Model):
    published = models.DateTimeField(auto_now_add=True,
                                     db_index=True, verbose_name='Дата/Время')
    user = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    name_product = models.ForeignKey('Product', related_name='product',
                                     verbose_name='Меню',
                                     null=True, on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество', default=1)
    summary = models.IntegerField(verbose_name='Оплачено', default=1)
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-published']


class Product(models.Model):
    slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1)
    name_product = models.CharField(max_length=100)
    count = models.IntegerField(verbose_name='Количество', default=1)
    price = models.IntegerField(verbose_name='Цена, BYN')


    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Меню'


class CheckList(models.Model):
    customer = Order.user
    product = Order.name_product
    paid = Order.summary
    comment = Order.comment
