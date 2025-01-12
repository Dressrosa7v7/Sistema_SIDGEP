# Generated by Django 4.1 on 2024-11-18 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoT', models.CharField(max_length=10)),
                ('Asset', models.CharField(max_length=20)),
                ('Paid', models.CharField(max_length=20)),
                ('Defeated', models.CharField(max_length=20)),
                ('InMora', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'PaymentStatus',
            },
        ),
    ]
