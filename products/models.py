from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-slug")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Изображение")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, 
                              related_name='children', verbose_name="Родительская категория")
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category_detail', args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название бренда")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-slug")
    logo = models.ImageField(upload_to='brands/', blank=True, null=True, verbose_name="Логотип")
    
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', 
                                verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', 
                             verbose_name="Бренд")
    name = models.CharField(max_length=200, verbose_name="Название товара")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-slug")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', 
                               verbose_name="Товар")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    is_main = models.BooleanField(default=False, verbose_name="Основное изображение")
    
    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
    
    def __str__(self):
        return f"Изображение для {self.product.name}"


class CategoryAttribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='attributes', 
                                verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название характеристики")
    unit = models.CharField(max_length=20, blank=True, verbose_name="Единица измерения")
    is_filterable = models.BooleanField(default=False, verbose_name="Используется для фильтрации")
    
    class Meta:
        verbose_name = "Характеристика категории"
        verbose_name_plural = "Характеристики категорий"
        unique_together = ('category', 'name')
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values', 
                               verbose_name="Товар")
    attribute = models.ForeignKey(CategoryAttribute, on_delete=models.CASCADE, 
                                 verbose_name="Характеристика")
    value = models.CharField(max_length=255, verbose_name="Значение")
    
    class Meta:
        verbose_name = "Значение характеристики"
        verbose_name_plural = "Значения характеристик"
        unique_together = ('product', 'attribute')
    
    def __str__(self):
        return f"{self.attribute.name}: {self.value} {self.attribute.unit}"
