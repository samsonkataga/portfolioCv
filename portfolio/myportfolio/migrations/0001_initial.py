# Generated by Django 4.1.4 on 2024-08-04 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
