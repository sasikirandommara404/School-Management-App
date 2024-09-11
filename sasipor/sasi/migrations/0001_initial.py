# Generated by Django 5.1.1 on 2024-09-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNumber', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('PhoneNumber', models.BigIntegerField()),
                ('Course', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('Gender', models.CharField(max_length=8)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=30)),
            ],
        ),
    ]
