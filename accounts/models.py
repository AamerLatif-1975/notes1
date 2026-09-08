from django.db import models


class StaffMember(models.Model):
    serial_number = models.IntegerField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    pay_scale = models.CharField(max_length=20)
    date_of_joining = models.DateField()
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
# Create your models here.
