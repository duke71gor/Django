# Generated by Django 2.2.2 on 2019-07-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190703_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_hot',
            field=models.BooleanField(default=False, verbose_name='горячий продукт'),
        ),
    ]