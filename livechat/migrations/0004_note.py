# Generated by Django 3.0.3 on 2020-03-07 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livechat', '0003_chatroom_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='livechat.ChatRoom')),
            ],
        ),
    ]