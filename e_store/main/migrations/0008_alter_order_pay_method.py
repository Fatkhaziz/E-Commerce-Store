# Generated by Django 4.1.4 on 2023-01-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_goods_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.CharField(choices=[('Visa', 'Visa'), ('MasterCard', 'MasterCard'), ('cash', 'cash')], max_length=10),
        ),
    ]
