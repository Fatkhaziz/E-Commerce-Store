# Generated by Django 4.1.4 on 2023-01-17 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_order_pay_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.CharField(choices=[('Visa', 'Visa'), ('cash', 'cash')], max_length=10),
        ),
    ]
