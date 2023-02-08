from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='название')
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Menu(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='название'
    )
    descr = models.CharField(
        max_length=2048,
        verbose_name='описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    image = models.ImageField(
        upload_to='menu/',
        verbose_name='картинка',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

class BookATable(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='название')
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )

