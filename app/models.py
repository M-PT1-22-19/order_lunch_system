from django.db import models

# Create your models here.

class Order(models.Model):
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата/Время')
    user = models.CharField(max_length=50, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    product = models.TextField(verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Количество')
    paid = models.FloatField(verbose_name='Оплачено')
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-published']
