# Generated by Django 4.2.8 on 2023-12-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
    ]
