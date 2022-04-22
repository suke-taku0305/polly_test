from django.db import models
import uuid

# Create your models here.
VOICE_CHOICES = [
    ('Takumi', '男性'),
    ('Mizuki', '女性'),
]

class Polly(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    talker = models.CharField(max_length=10, choices=VOICE_CHOICES)
    remark = models.TextField(max_length=400)
    audio = models.FileField(upload_to="polly_speech", blank=True, null=True)