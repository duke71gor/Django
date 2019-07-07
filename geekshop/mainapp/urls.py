from django.urls import path
from mainapp.views import products
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('category/<int:pk>/', products, name='category'),
#   path('product/<int:pk>/', mainapp.product, name='product'),
]
