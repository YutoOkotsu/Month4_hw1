# Generated by Django 4.2.10 on 2024-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0002_alter_shoe_image_1_alter_shoe_image_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='created_by',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='shoe',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='Напишите сюда бренд'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='category',
            field=models.CharField(max_length=1000, verbose_name='Напишите для какой задачи сделаны кроссовки'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='model',
            field=models.CharField(max_length=1000, verbose_name='Напишите какая модель кроссовка'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.CharField(max_length=100, verbose_name='Напишите какие размеры доступны'),
        ),
    ]
