# Generated by Django 4.1.3 on 2022-11-30 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='productvaraiant',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
        migrations.AlterField(
            model_name='productvaraiant',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.colour'),
        ),
        migrations.AlterField(
            model_name='productvaraiant',
            name='size',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.size'),
        ),
    ]
