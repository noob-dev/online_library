# Generated by Django 5.1.1 on 2024-10-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_rename_publication_date_book_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
