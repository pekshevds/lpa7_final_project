# Generated by Django 4.1 on 2024-10-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lpa7user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='lpa7user',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='birth day'),
        ),
        migrations.AddField(
            model_name='lpa7user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='avatar'),
        ),
        migrations.AddField(
            model_name='lpa7user',
            name='name',
            field=models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='name'),
        ),
    ]
