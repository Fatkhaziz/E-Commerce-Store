# Generated by Django 4.1.4 on 2023-01-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=2, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Visa', 'Visa'), ('MasterCard', 'MasterCard'), ('PayPal', 'PayPal')], max_length=10),
        ),
    ]
