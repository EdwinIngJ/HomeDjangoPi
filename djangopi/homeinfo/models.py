from django.db import models

# Create your models here.
class ToggleWatering(models.Model):
    auto = models.BooleanField(default=False)
    manual = models.BooleanField(default=False)

    def __str__(self):
        return "Auto: {}, Manual: {}".format(self.auto, self.manual)


class Log(models.Model):
    log = models.TextField()
    time_watered = models.DateTimeField()

    def __str__(self):
        return self.log
