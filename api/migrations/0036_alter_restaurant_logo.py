# Generated by Django 5.1.1 on 2024-10-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_alter_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(default=None, upload_to='restaurant_logos/'),
        ),
    ]
