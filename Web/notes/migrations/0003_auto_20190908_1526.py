# Generated by Django 2.2.4 on 2019-09-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
