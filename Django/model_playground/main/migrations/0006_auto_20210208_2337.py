# Generated by Django 3.1.6 on 2021-02-08 18:07

import django.core.validators
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(3), main.validators.validate_even_number]),
        ),
    ]
