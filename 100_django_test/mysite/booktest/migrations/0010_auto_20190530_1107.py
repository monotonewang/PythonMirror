# Generated by Django 2.2 on 2019-05-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0009_auto_20190530_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='bpub_titile',
            field=models.DateField(auto_now_add=True, db_column='b_pub_date'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hcomment',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
