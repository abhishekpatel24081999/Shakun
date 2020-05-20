from django.db import models
from Owner.models import Product,City
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    fname = models.CharField(("Enter First Name"), max_length=50,blank=True)
    lname = models.CharField(("Enter Last Name"), max_length=50,blank=True)
    img = models.ImageField(("Insert Image"), upload_to="user",blank=True)
    # , height_field=None, width_field=None, max_length=None
    img_thumb = ImageSpecField(source='img',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
    contact = models.PositiveIntegerField(("Enter Phone No. :-"),null=True,blank=True)

    def __str__(self):
        return self.fname+" "+self.lname


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=("Select User"), on_delete=models.CASCADE,default="")
    product = models.ForeignKey(Product, verbose_name=("Select Product"), on_delete=models.CASCADE,default="")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=("Select User"), on_delete=models.CASCADE,default="")
    address = models.TextField(("Enter Address"))
    village = models.CharField(("Enter Village Name"), max_length=50)
    pin = models.PositiveIntegerField(("Enter PinCode No."),null = True ,blank = True)
    created_at = models.DateTimeField(auto_now_add=True,null = True,blank=True)
    def __str__(self):
        return self.village

DAY_CHOICES = (
    (0, 'Aftrer One Day'),
    (1, 'After two Day'),
    (2, 'After Three Day'),
    (3, 'After Four Day'),
    (4, 'After Five Day'),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, verbose_name=("Select User"), on_delete=models.CASCADE,default="")
    product = models.ForeignKey(Product, verbose_name=("Select Product"), on_delete=models.CASCADE,default="")
    address = models.ForeignKey(Address, verbose_name=("Select Address"), on_delete=models.CASCADE,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    day = models.CharField(max_length=1, choices=DAY_CHOICES)
    status = models.BooleanField(("Conform ?"),default=False)
    c_status = models.BooleanField(("Conformed ?"),default=False)
    done = models.BooleanField(("Complete?"),default=False)
    amount = models.PositiveIntegerField(("Final Amount"),default=0)
    advance_amount = models.PositiveIntegerField(("Advance Pay"),default=0)
    advance_pay_s = models.BooleanField(("Advance Pay Status"),default=False)
    last_amount = models.PositiveIntegerField(("Last Pay"),default=False)
    last_pay_s = models.BooleanField(("Advance Pay Status"),default=False)
    feedback_status = models.BooleanField(("Feedback Sataus"),default=False)
    reject = models.BooleanField(("Reject???"),default=False) 
    reject_resion = models.CharField(("Reject Resion"), max_length=150,null = True,blank=True)
    def __str__(self):
        return self.product.name

class Transaction(models.Model):
    appointment = models.ForeignKey(Appointment, verbose_name=("Appointment ID"), on_delete=models.CASCADE)
    TXNID = models.CharField(("Trasiction ID"),max_length=150)
    TXNAMOUNT = models.FloatField(("Transicton Amount"),default=0)
    PAYMENTMODE = models.CharField(("Payment Mode"), max_length=50,default="")
    CURRENCY = models.CharField(("Currency of payment mode"), max_length=50,default="")
    STATUS = models.BooleanField(("Payment Status"),default=False)
    GATEWAYMODE = models.CharField(("Gateway Mode"), max_length=50,default="")
    BANKTXNID = models.CharField(("Bank ID"), max_length=50,default="")
    BANKNAME = models.CharField(("Bank Name"), max_length=50,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ("Transaction")
        verbose_name_plural = ("Transactions")

    def __str__(self):
        return self.name


class Location(models.Model):
    user = models.ForeignKey(User, verbose_name=("Select User"), on_delete=models.CASCADE)
    city = models.CharField(("Enter City"), max_length=50)

    class Meta:
        verbose_name = ("Location")
        verbose_name_plural = ("Locations")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})




    def get_absolute_url(self):
        return reverse("Transaction_detail", kwargs={"pk": self.pk})

class Feedback(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=("Select Customer"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Select Product"), on_delete=models.CASCADE)
    feed = RichTextUploadingField()

    class Meta:
        verbose_name = ("Feedback")
        verbose_name_plural = ("Feedbacks")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Feedback_detail", kwargs={"pk": self.pk})
