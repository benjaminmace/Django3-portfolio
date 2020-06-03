# Generated by Django 3.0.5 on 2020-06-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
