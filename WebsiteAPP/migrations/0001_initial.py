# Generated by Django 5.1.2 on 2024-10-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contact_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact_Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact_TextArea', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
