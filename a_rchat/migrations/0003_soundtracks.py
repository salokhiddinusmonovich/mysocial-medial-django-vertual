# Generated by Django 5.0.6 on 2024-06-11 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rchat', '0002_chatgroup_user_online'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundTracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('sound', models.FileField(upload_to='sounds/')),
            ],
        ),
    ]