# Generated by Django 3.1.7 on 2021-04-07 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='board',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='quests.questboard'),
        ),
    ]
