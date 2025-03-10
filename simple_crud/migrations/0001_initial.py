# Generated by Django 5.1.6 on 2025-03-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimpleCRUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_item', models.CharField(max_length=255, verbose_name='Name of register')),
                ('quantity_item', models.IntegerField(verbose_name='Quantity of register')),
                ('have_item', models.BooleanField(default=True, verbose_name='Have the item in the register?')),
            ],
            options={
                'db_table': 'simple_crud',
            },
        ),
    ]
