# Generated by Django 5.0.4 on 2024-05-03 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_link', models.TextField()),
                ('short_link', models.CharField(max_length=128)),
            ],
        ),
    ]