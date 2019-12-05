# Generated by Django 2.0.6 on 2019-12-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('initial', models.CharField(max_length=1)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=5)),
            ],
        ),
    ]