from django.db import models

class TimeSetting(models.Model):
    watt = models.IntegerField()
    timestamp = models.TimeField()

    def __str__(self):
        return self.timestamp.strftime("%H:%M:%S") + ": " + str(self.watt)
 