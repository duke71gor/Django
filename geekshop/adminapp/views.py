from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import Product, ProductCategory
from .forms import ProductAdminForm
from authapp.models import ShopUser


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


#Products:

class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    #список объетов по умолчанию. Берет все объекты из списка продуктов
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if self.kwargs.get('category_pk'):
            queryset = queryset.filter(category=self.kwargs.get('category_pk'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Все продукты. Админка'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}.Админка'.format(title)
        return context


class ProductCreateView(IsSuperUserView, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'СозданНовПрод.Админка'
        return context


class ProductDeleteView(IsSuperUserView, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}.Админка'.format(title)
        return context


class ProductUpdateView(IsSuperUserView, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    form_class = ProductAdminForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Изменение {}.Админка'.format(title)
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk': self.kwargs.get('pk')})


#Categories:

class CategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'СозданНовКат.Админка'
        return context


class CategoryUpdateView(IsSuperUserView, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Изменение категории {}.Админка'.format(title)
        return context


class CategoryDeleteView(IsSuperUserView, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}.Админка'.format(title)
        return context


    #Users:

class UsersListView(IsSuperUserView, ListView):
    model = ShopUser
    template_name = 'adminapp/shopusers.html'
    fields = 'username'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'Все пользователи. Админка'
        context['users'] = ShopUser.objects.all()
        return context


class UserCreateView(IsSuperUserView, CreateView):
    model = ShopUser
    template_name = 'adminapp/register.html'
    success_url = reverse_lazy('admin_custom:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'СозданНовПользов.Админка'
        return context


class UserUpdateView(IsSuperUserView, UpdateView):
    model = ShopUser
    template_name = 'adminapp/register.html'
    fields = 'username', 'email', 'avatar', 'age'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Изменение пользователя {}.Админка'.format(title)
        return context


class UserDeleteView(IsSuperUserView, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Удаление {}.Админка'.format(title)
        return context