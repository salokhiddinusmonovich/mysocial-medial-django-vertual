# Generated by Django 5.0.6 on 2024-06-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rchat', '0008_remove_privatemessage_chat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
