# Generated by Django 3.1.7 on 2021-03-12 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20210312_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoraf Ekleyin'),
        ),
    ]
