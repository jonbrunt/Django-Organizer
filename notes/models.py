from uuid import uuid4
from django.db import models

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    content = models.CharField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    