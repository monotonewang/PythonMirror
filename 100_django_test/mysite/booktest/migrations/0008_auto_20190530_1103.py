# Generated by Django 2.2 on 2019-05-30 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0007_auto_20190530_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_titile',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]