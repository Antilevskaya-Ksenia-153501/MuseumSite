# Generated by Django 4.2.5 on 2023-09-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0004_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateField(),
        ),
    ]
