import uuid
from django.db import models
from django.utils import timezone
# Create your models here.


class sendEmail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=50, blank=False)
    datos = models.CharField(max_length=500, blank=True)
    completo = models.BooleanField(default=False)
    fecha_espera = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        verbose_name = "Email"

    def __str__(self):
        return self.email