# Generated by Django 3.0.3 on 2020-03-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='thread',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
