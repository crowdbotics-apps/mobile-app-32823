from django.conf import settings
from django.db import models


class Account(models.Model):
    "Generated Model"
    acc_no = models.BigIntegerField()
    account_name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
