# Generated by Django 4.1 on 2024-11-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoP', models.CharField(max_length=10)),
                ('Monthly', models.CharField(max_length=200)),
                ('Weekly', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'PaymentFrecuency',
            },
        ),
    ]
