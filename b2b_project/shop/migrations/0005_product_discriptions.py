# Generated by Django 4.0.5 on 2022-07-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_category_alter_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discriptions',
            field=models.TextField(default='name'),
            preserve_default=False,
        ),
    ]
