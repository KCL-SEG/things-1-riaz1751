# Generated by Django 4.1.2 on 2022-10-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('things', '0003_delete_thing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('age', models.TextField()),
            ],
        ),
    ]
