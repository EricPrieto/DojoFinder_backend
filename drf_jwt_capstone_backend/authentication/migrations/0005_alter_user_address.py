# Generated by Django 3.2.8 on 2021-12-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
