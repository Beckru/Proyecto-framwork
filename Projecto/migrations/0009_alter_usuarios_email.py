# Generated by Django 4.1.3 on 2023-01-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projecto', '0008_alter_publicacion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
