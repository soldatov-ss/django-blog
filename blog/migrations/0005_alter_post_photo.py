# Generated by Django 4.0.1 on 2022-02-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_created_at_alter_post_updated_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изображение'),
        ),
    ]