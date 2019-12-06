# Generated by Django 2.1.1 on 2019-12-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_title', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('time', models.TimeField()),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
