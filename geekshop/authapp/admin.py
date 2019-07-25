from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot

#Inline штуки:
class BasketInline(admin.TabularInline):
    model = BasketSlot
    fields = 'product', 'quantity'
    extra = 1

#Первичная настройка:
@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    list_display = 'username', 'is_superuser',
    list_filter = 'is_superuser',
    search_fields = 'username',
    readonly_fields = 'password',

#Proxy - для назначения двух и больше админок на одну и ту же модель
class UsersWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True

@admin.register(UsersWithBasket)
class UsersWithBasketAdmin(admin.ModelAdmin):
    fields = 'username',
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost'
    list_filter = 'is_superuser',
    search_fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInline,

    #Ограничение queryset:
    def get_queryset(self, request):
        qs = super(UsersWithBasketAdmin, self).get_queryset(request)
        return qs.filter(basket__quantity__gt=0).distinct()

    #свои произвольные функциональные поля:
    def get_basket_quantity(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
    get_basket_quantity.short_description = 'Товаров в корзине'

    def get_basket_cost(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot: basket_slot.cost, basket)))
    get_basket_cost.short_description = 'Стоимость корзины (руб)'