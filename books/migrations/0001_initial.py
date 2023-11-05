# Generated by Django 4.2.7 on 2023-11-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
                ('type_car', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=4)),
                ('used', models.BooleanField(default=True)),
                ('price', models.CharField(max_length=20)),
                ('register', models.DateTimeField(auto_now_add=True)),
                ('image_url', models.CharField(max_length=300)),
            ],
        ),
    ]
