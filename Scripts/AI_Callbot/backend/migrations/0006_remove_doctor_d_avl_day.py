# Generated by Django 5.1.2 on 2024-10-26 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_doctor_d_avl_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='D_Avl_Day',
        ),
    ]
