# Generated by Django 3.0.3 on 2020-02-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200229_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_doc',
            field=models.BooleanField(default=False),
        ),
    ]
