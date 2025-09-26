from django.db import models

from users.models import User


class Note(models.Model):
    name = models.CharField(max_length=50, verbose_name="Запись")
    text = models.TextField(blank=True, null=True, verbose_name="Содержимое записи")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.name
