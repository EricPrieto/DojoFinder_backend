# Generated by Django 3.2.8 on 2021-12-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practitioners', '0003_alter_practitioner_school_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practitioner',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
