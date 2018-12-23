from django.db import models

# Create your models here.
ALARM_STATUS = (
    ('new', 'NEW'),
    ('checked', 'CHECKED'),
)

ALARM_TYPE = (
    ('video', 'VIDEO'),
    ('image', 'IMAGE'),
    ('attached', 'ATTACHED'),
)

# alarm data
class Alarm(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    alarm_type = models.CharField(max_length=10, choices=ALARM_TYPE, default="NONE")
    url = models.URLField(max_length=2048, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10, choices=ALARM_STATUS, default="new")

    def __str__(self):
        return self.status + '->' + self.title
