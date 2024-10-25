# Generated by Django 5.1.2 on 2024-10-25 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_department_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Dept_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='D_Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.department'),
        ),
    ]
