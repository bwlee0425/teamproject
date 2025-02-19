# Generated by Django 5.1.3 on 2025-02-19 09:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0005_alter_payment_pay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_date',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date(2025, 2, 19))]),
        ),
    ]
