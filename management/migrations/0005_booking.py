# Generated by Django 4.2.5 on 2023-09-30 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=500)),
                ('p_phone', models.IntegerField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('doc_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.doctor')),
            ],
        ),
    ]
