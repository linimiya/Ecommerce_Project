# Generated by Django 5.1.2 on 2024-11-22 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteAPP', '0008_alter_cart_db_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_db',
            name='Prod_Img',
            field=models.ImageField(blank=True, null=True, upload_to='Cart_Images'),
        ),
    ]
