from django.db import models

class RawScores(models.Model):
    name = models.CharField(max_length=-1)
    zip = models.TextField() # This field type is a guess.
    inspect_date = models.CharField(max_length=-1)
    score = models.SmallIntegerField()
    address = models.CharField(max_length=-1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        db_table = u'raw_scores'
