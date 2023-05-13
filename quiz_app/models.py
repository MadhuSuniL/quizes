from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    quesion = models.CharField(max_length=500)
    options = models.JSONField()
    answer = models.CharField(max_length=1000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    starts_date = models.DateField()
    starts_time = models.TimeField()
    ends_date = models.DateField()
    ends_time = models.TimeField()
    status = models.CharField(max_length=50)
    
    def update_status(self):
        current_datetime = timezone.now()

        if self.starts_date <= current_datetime.date() <= self.ends_date:
            if current_datetime.time() <= self.ends_time:
                self.status = "Active"
            elif current_datetime.time() < self.starts_time:
                self.status = "Upcoming"
            else:
                self.status = "Expired"
        else:
            self.status = "Inactive"

        self.save()