# Generated by Django 3.1.4 on 2021-03-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210322_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(),
        ),
    ]
