# Generated by Django 3.1.4 on 2021-09-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20201211_1253'),
        ('app', '0014_remove_workout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile'),
        ),
    ]
