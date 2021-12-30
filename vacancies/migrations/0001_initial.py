# Generated by Django 3.2.10 on 2021-12-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('length', models.FloatField()),
            ],
        ),
    ]