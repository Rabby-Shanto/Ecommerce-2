# Generated by Django 4.1.3 on 2022-12-02 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvaraiant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='shop.product'),
        ),
    ]