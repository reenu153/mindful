# Generated by Django 3.0.3 on 2020-03-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionaire', '0003_auto_20200306_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.IntegerField(choices=[(2, 'Never'), (1, 'Rarely'), (0, 'Sometimes'), (-1, 'Often'), (-2, 'Very Often')]),
        ),
    ]
