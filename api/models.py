from django.db import models
from django.utils.translation import gettext_lazy as _


class Parking(models.Model):
    name = models.CharField(max_length=30, unique=True)
    address = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.name, self.address)


class ParkingSpace(models.Model):
    code = models.CharField(max_length=20)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

    class Status(models.TextChoices):
        EMPTY = 'EM', _('Empty')
        FULL = 'FL', _('Full')
        BOOKED = 'BK', _('Booked')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.EMPTY,
    )

    def __str__(self):
        return "%s %s" % (self.code, self.parking.name)
