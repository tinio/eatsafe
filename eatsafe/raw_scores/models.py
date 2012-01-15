from django.db import models

class RawScore(models.Model):
    name = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)
    inspect_date = models.CharField(max_length=255)
    score = models.SmallIntegerField()
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    class Meta:
        db_table = u'raw_scores'

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.inspect_date)
