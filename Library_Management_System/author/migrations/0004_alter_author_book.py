# Generated by Django 4.0.4 on 2022-05-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_admin', '0006_alter_issued_book_return_date_and_more'),
        ('author', '0003_alter_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='author', to='library_admin.book'),
        ),
    ]
