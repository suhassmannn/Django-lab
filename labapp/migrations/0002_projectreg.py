# Generated by Django 5.0.7 on 2024-07-22 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=30)),
                ('planguage', models.CharField(max_length=30)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.student')),
            ],
        ),
    ]
