# Generated by Django 2.2 on 2019-05-30 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0006_auto_20190530_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
