# Generated by Django 4.2.10 on 2024-03-04 10:17

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(default='+996', max_length=13, verbose_name='Введите номер телефона')),
                ('date_birth', models.DateField(verbose_name='Ваша дата рождения')),
                ('gender', models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], max_length=20, verbose_name='Укажите пол')),
                ('favorite_color', models.CharField(choices=[('красный', 'Красный'), ('зеленый', 'Зеленый'), ('синий', 'Синий'), ('желтый', 'Желтый'), ('черный', 'Черный'), ('белый', 'Белый')], max_length=255, verbose_name='Любимый цвет')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('organization', models.CharField(max_length=255, verbose_name='Организация')),
                ('consent', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SMSCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sms_codes', to='users.customuser')),
            ],
        ),
    ]
