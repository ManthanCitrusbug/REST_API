# Generated by Django 3.1.4 on 2022-05-18 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220517_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=70, null=True, unique=True),
        ),
    ]