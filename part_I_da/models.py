from otree.api import *
#c = cu

doc = ''
class Constants(BaseConstants):
    name_in_url = 'part_I_da'
    players_per_group = None
    num_rounds = 1
    timer_seconds = 300
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass

class Player(BasePlayer):

    ctrq1_da = models.IntegerField(label='Wie viele Schüler:innen bewerben sich für einen Schulplatz?', min=0)
    ctrq2_da = models.IntegerField(label='Wie viele Plätze bleiben übrig, sobald alle Schüler:innen an einer Schule zugelassen wurden?', min=0)
    time_left = models.IntegerField(initial=Constants.timer_seconds)
    ctrq3_da_blue = models.StringField(choices=['A', 'B', 'C', 'D'], label='')
    ctrq3_da_yellow = models.StringField(choices=['A', 'B', 'C', 'D'], label='')
    ctrq3_da_orange = models.StringField(choices=['A', 'B', 'C', 'D'], label='')
    ctrq3_da_purple = models.StringField(choices=['A', 'B', 'C', 'D'], label='')
    mc1_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='1. Bei der Entscheidung, welche Präferenzliste man an die zentrale Zulassungsstelle übermittelt, sollte man darauf achten, dass man sich nicht bei der beliebtesten Schule zuerst bewirbt.')
    mc2_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='2. Es ist ausschlaggebend für die Erstellung der eigenen Präferenzliste, die Wertetabelle für alle anderen Schüler:innen zu kennen.')
    mc3_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='3. Das Zulassungsverfahren ist so konstruiert, dass die übermittelte Präferenzliste immer mit der Reihenfolge übereinstimmen sollte, die sich aus der Wertetabelle ergibt.')
    mc4_da = models.StringField(choices=['Richtig', 'Falsch'],
                                label='4. Ihre Präferenzliste sollte nur mit der Reihenfolge aus der Wertetabelle übereinstimmen, wenn Sie sicher sind, dass alle Schüler:innen ebenso verfahren.')