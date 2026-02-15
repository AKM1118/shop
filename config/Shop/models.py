from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Поле для хранения строк
    image = models.ImageField(upload_to='images/Product/')  # Поле для изображений
    desc = models.TextField()  # Текстовое поле без ограничения длины
    price = models.FloatField()  # Число с плавающей точкой
    discount = models.PositiveIntegerField(default=0)  # Положительное целое число
    rating = models.PositiveIntegerField()  # Оценка товара
    stock = models.PositiveIntegerField()  # Количество на складе
    is_available = models.BooleanField(default=True)  # Доступность товара