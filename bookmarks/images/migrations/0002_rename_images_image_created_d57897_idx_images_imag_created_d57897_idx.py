# Generated by Django 5.1.4 on 2024-12-24 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='image',
            new_name='images_image_created_d57897_idx',
            old_name='images_image_created_d57897_idx',
        ),
    ]