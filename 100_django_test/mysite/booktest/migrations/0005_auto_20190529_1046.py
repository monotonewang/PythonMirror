# Generated by Django 2.2 on 2019-05-29 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0004_bookinfo_isdelete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='isDelete',
            new_name='bdelete',
        ),
        migrations.AddField(
            model_name='heroinfo',
            name='hdelete',
            field=models.BooleanField(default=False),
        ),
    ]