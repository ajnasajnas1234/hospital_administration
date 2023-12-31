# Generated by Django 4.2.5 on 2023-09-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=500)),
                ('p_phone', models.IntegerField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('doc_name', models.CharField(max_length=500)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
