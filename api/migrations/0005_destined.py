# Generated by Django 2.2.16 on 2020-11-18 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_apiurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characters', models.URLField()),
            ],
        ),
    ]
