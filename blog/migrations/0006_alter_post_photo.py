# Generated by Django 4.0.1 on 2022-02-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]
