from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html', {'username': 'Vanya', 'array': [1, 2, 3, 4, 5]})

def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    title = ['Главная', 'Каталог', 'Контакты']
    same_products = ['products_all', 'products_home', 'products_office', 'products_modern', 'products_classic']
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }
    return render(request, 'mainapp/products.html', content)

def contact(request):
    return render(request, 'mainapp/contact.html')