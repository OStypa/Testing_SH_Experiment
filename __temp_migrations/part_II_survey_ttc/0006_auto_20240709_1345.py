# Generated by Django 2.2.12 on 2024-07-09 11:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_II_survey_ttc', '0005_auto_20240709_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='abi_grade',
            field=otree.db.models.FloatField(null=True, verbose_name='Mit welcher Note haben Sie Ihren höchsten Schulabschluss beendet (z.B. Abitur, Mittlere Reife, ...)?'),
        ),
    ]
