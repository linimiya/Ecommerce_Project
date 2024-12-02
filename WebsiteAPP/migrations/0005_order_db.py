# Generated by Django 5.1.2 on 2024-11-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteAPP', '0004_alter_cart_db_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Message', models.TextField(blank=True, max_length=100, null=True)),
                ('Sub_Total', models.IntegerField(blank=True, null=True)),
                ('Shipping_Price', models.IntegerField(blank=True, null=True)),
                ('Final_Pay', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
