# Generated by Django 5.1.1 on 2024-10-19 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='published_date',
        ),
    ]
