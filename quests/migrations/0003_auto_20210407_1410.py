# Generated by Django 3.1.7 on 2021-04-07 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0002_addquest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateQuestboard',
            new_name='Quest',
        ),
        migrations.RenameModel(
            old_name='AddQuest',
            new_name='Questboard',
        ),
    ]
