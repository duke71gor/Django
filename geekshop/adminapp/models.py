from django.db import models
#from django.contrib.auth.models import AbstractUser


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)


#class ShopUser(AbstractUser):
#    class Meta:
#        verbose_name = 'пользователь'
#        verbose_name_plural = 'пользователи'

#    avatar = models.ImageField(upload_to='users_avatars', blank=True)
#    age = models.PositiveIntegerField(verbose_name='возраст')

#   def __str__(self):
#        return self.username

