# Generated by Django 4.2.5 on 2023-09-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_phone',
            field=models.IntegerField(),
        ),
    ]
