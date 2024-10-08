# Generated by Django 2.2.12 on 2024-07-11 15:16

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_II_survey_ttc_adv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='crt_bat',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Ein Schläger und ein Ball kosten insgesamt 1,10 €. Der Schläger kostet 1 € mehr als der Ball. Wie viel kostet der Ball?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='crt_lake',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='In einem See wachsen Seerosen, die sich jeden Tag verdoppeln. Wenn es 48 Tage dauert, bis der ganze See bedeckt ist, wie lange dauert es, bis die Seerosen die Hälfte des Sees bedecken?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='crt_widget',
            field=otree.db.models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Wenn 5 Maschinen 5 Minuten brauchen um 5 Produkte herzustellen, wie lange benötigen dann 100 Maschinen, um 100 Produkte herzustellen?'),
        ),
    ]
