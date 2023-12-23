from django.db import models
from datetime import datetime
now = datetime.now()
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    is_completed  = models.BooleanField(default=True)
    created_at   = models.DateTimeField(db_default=now)
    updated_at   = models.DateTimeField(db_default=now)

    def __str__(self):
        return self.title