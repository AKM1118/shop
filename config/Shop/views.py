from django.shortcuts import render
from .models import Product
def catalog(request):
# Получаем все товары из базы данных
    products = Product.objects.all()
    
    # Передаём их в контекст
    return render(request, 'shop/catalog.html', {'products': products})
