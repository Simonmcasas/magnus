# Generated by Django 4.2.6 on 2023-10-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
