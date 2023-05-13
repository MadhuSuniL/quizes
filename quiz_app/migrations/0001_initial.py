# Generated by Django 4.2.1 on 2023-05-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesion', models.CharField(max_length=500)),
                ('options', models.JSONField()),
                ('answer', models.CharField(max_length=1000)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('starts_date', models.DateField()),
                ('starts_time', models.TimeField()),
                ('ends_date', models.DateField()),
                ('ends_time', models.TimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
