# Generated by Django 2.2.2 on 2019-07-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_product_is_hot'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dis',
            field=models.PositiveIntegerField(default=0, verbose_name='скидка %'),
        ),
    ]