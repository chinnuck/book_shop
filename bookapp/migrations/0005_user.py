# Generated by Django 5.1.2 on 2024-10-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_alter_cart_cart_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('user_phone', models.CharField(max_length=11)),
                ('user_password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
