# Generated by Django 3.0.8 on 2020-08-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_long', models.CharField(max_length=400)),
                ('short', models.CharField(max_length=100)),
            ],
        ),
    ]