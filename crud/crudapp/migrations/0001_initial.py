# Generated by Django 4.2.2 on 2023-06-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.IntegerField()),
                ('Item_name', models.CharField(max_length=250)),
                ('Description', models.TextField()),
            ],
        ),
    ]
