# Generated by Django 3.0.3 on 2020-03-06 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0005_patientdata_lifestyle_quiz_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddata',
            old_name='apettite',
            new_name='appetite',
        ),
    ]