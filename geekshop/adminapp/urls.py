import adminapp.views as adminapp
from django.urls import path


app_name = 'adminapp'

urlpatterns = [
    #path('users/create/', adminapp.user_create, name='user_create'),
    #path('users/read/', adminapp.UsersListView, name='users'),
    #path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    #path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.ProductListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    #path('categories/delete/<int:pk>/', adminapp.CategoryDeleteVIew.as_view(), name='category_delete'),

    path('prudcuts/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]