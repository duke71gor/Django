from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from random import randint

def main(request):
    context = {'username': 'alexey'}
    return render(request, 'mainapp/main.html', context)

def products(request, pk=None):
    products = Product.objects.all()

    if pk or pk == 0:
        if pk != 0:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = products.filter(category=category)
        context = {'products': products, 'categories': ProductCategory.objects.all()}
        return render(request, 'mainapp/products.html', context)
    else:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {'hot_product': hot_product, 'categories': ProductCategory.objects.all()}
        return render(request, 'mainapp/hot_product.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')

#def discount(request): #функция рендомного дискаунта на горячий товар от 3 до 60 %
#    dis = randint(3, 61)
 #   context = {'discount': dis}
 #   return render(request, 'mainapp/hot_product.html', context)



#функция отдельного продукта
#def product(request, pk):
#    title = 'продукты'
#
#    context = {
#        'title': title,
#        'links_menu': ProductCategory.objects.all(),
#        'product': get_object_or_404(Product, pk=pk),
#        'basket': get_basket(request.user), #проблемная get_basket
#    }
#
#    return render(request, 'mainapp/product.html', context)
