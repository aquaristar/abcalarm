from django.db import models

# Create your models here.
ALARM_STATUS = (
    ('new', 'NEW'),
    ('checked', 'CHECKED'),
)


# alarm data
class Alarm(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=2048, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10, choices=ALARM_STATUS, default="NONE")

    def __str__(self):
        return self.status + '->' + self.title
