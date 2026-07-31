from django.db import models

from common.models import BaseModel


class Variable(BaseModel):
    """
    Master Variable
    """

    code = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        verbose_name="Variable Code"
    )

    name = models.CharField(
    max_length=100,
    unique=True,
    db_index=True,
    verbose_name="Variable Name"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description"
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=1.00,
        verbose_name="Weight"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Active"
    )

    class Meta:
        db_table = "master_variable"
        verbose_name = "Variable"
        verbose_name_plural = "Variables"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.name}"