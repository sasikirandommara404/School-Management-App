# Generated by Django 5.1.1 on 2024-09-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RollNumber', models.CharField(max_length=30)),
                ('Telugu', models.IntegerField()),
                ('Hindi', models.IntegerField()),
                ('English', models.IntegerField()),
                ('Maths', models.IntegerField()),
                ('Physics', models.IntegerField()),
                ('Chemistry', models.IntegerField()),
                ('Science', models.IntegerField()),
                ('Social', models.IntegerField()),
            ],
        ),
    ]
