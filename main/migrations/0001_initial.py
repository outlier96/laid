# Generated by Django 3.2.15 on 2023-01-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('tel', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=250)),
                ('bauth', models.CharField(max_length=12)),
                ('adnum', models.CharField(max_length=10)),
                ('userid', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='id')),
            ],
        ),
    ]
