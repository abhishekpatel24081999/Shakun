from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from Customer.models import *
from Owner.models import *
from django.contrib.auth.models import User

# Create your models here.

class ManageAppointment(models.Model):
    appointment = models.OneToOneField(Appointment, verbose_name=(""), on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, verbose_name=(""), on_delete=models.CASCADE)
    status = models.BooleanField(("Conformed?"),default=False,null=True,blank=True)
    reject = models.BooleanField(("Reject?"),default=False)
    class Meta:
        verbose_name = ("ManageAppointment")
        verbose_name_plural = ("ManageAppointments")

    def __str__(self):
        return self.appointment.product.name

    def get_absolute_url(self):
        return reverse("ManageAppointment_detail", kwargs={"pk": self.pk})


class Conform(models.Model):
    manageAppointment = models.OneToOneField(ManageAppointment, verbose_name=("Select Appointment"), on_delete=models.CASCADE)
    note = models.TextField(("Enter Note"),default=None,null=True,blank=True)
    file = models.FileField(("Drop File"), upload_to="conform" ,max_length=100,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Conform")
        verbose_name_plural = ("Conforms")

    def __str__(self):
        return self.note

    def get_absolute_url(self):
        return reverse("Conform_detail", kwargs={"pk": self.pk})

