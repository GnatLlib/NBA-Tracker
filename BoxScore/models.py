from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class QuarterScore(models.Model):
    team_1 = models.CharField(max_length=200)
    team_2 = models.CharField(max_length=200)

    t1_q1 = models.IntegerField()
    t1_q2 = models.IntegerField()
    t1_q3 = models.IntegerField()
    t1_q4 = models.IntegerField()
    t1_total = models.IntegerField()

    t2_q1 = models.IntegerField()
    t2_q2 = models.IntegerField()
    t2_q3 = models.IntegerField()
    t2_q4 = models.IntegerField()
    t2_total = models.IntegerField()

    game_id = models.IntegerField(primary_key=True)
    game_date = models.DateField(blank=True)

    def __str__(self):
        return str(self.game_id)


