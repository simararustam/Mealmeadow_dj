# Generated by Django 5.1.1 on 2024-10-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_rename_image_url_food_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
