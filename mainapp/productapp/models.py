from django.db import models


class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Бренд',
        unique=True,
        default=None,
    )

    image = models.ImageField(
        upload_to='brand_images',
        default=True,
    )

    is_active = models.BooleanField(
        verbose_name='Стояние',
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brands'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        max_length=100,
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='Стояние',
        default=True,
    )

    image = models.ImageField(
        upload_to='category_images',
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genders(models.Model):
    name = models.CharField(
        verbose_name='Пол',
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'gender'
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        max_length=100,
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
    )

    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=0,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Остаток',
        default=0
    )

    gender = models.ForeignKey(
        Genders,
        on_delete=models.CASCADE,
        default=None
    )

    image = models.ImageField(
        upload_to='product_images',
        default=True,
    )

    is_active = models.BooleanField(
        verbose_name='Статус',
        default=True,
    )

    def __str__(self):
        return f'{self.name}-{self.pk}'

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Gallery(models.Model):
    image = models.ImageField(
        upload_to='product_images',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='gallery'

    )
