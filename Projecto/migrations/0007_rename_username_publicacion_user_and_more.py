# Generated by Django 4.1.3 on 2023-01-05 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Projecto', '0006_publicacion_name_publi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='name_publi',
        ),
    ]