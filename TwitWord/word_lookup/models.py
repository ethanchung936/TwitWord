from tkinter.filedialog import test
from django.db import models
import uuid

class WordTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=100)
    def __str__(self):
        return self.word

