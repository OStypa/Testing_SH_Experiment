# Generated by Django 2.2.12 on 2024-07-15 19:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_II_survey_da3', '0002_auto_20240715_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='risk',
            field=otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='\n        Wie nehmen Sie sich selbst wahr? \n        Sind Sie generell ein Mensch, der voll und ganz bereit ist, Risiken einzugehen (10), oder versuchen Sie eher, Risiken zu vermeiden (0)?'),
        ),
    ]
