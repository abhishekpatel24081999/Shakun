from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class City(models.Model):
    name = models.CharField(("Enter City Name"), max_length=50,default="",unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(("Enter Category Name"), max_length=50,default="")
    disc = models.TextField(("Discription about Category"))

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name


class Owner(models.Model):
    user = models.OneToOneField(User, verbose_name=("Select User"), on_delete=models.CASCADE)
    fname = models.CharField(("Enter First Name"), max_length=50)
    lname = models.CharField(("Enter Last Name"), max_length=50)
    img = models.ImageField(("Insert Image"), upload_to="owner")
    contact = models.PositiveIntegerField()
    email = models.EmailField(max_length=254,default = "")
    # , height_field=None, width_field=None, max_length=None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, verbose_name=("Select City"), on_delete=models.CASCADE,default="",null=True,blank=True)
    img_thumb = ImageSpecField(source='img',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
    def __str__(self):
        return self.fname + " " +self.lname

class Product(models.Model):
    owner = models.ForeignKey(Owner, verbose_name=("Select Owner"), on_delete=models.CASCADE,default="")
    name = models.CharField(("Enter Product Name"), max_length=50)
    category = models.ForeignKey(Category, verbose_name=("Select Category"), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(("Insert Image"), upload_to="product")
    # , height_field=None, width_field=None, max_length=None
    img_thumb = ImageSpecField(source='img',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 100})
    price = models.IntegerField(("Enter Price"))
    disc = RichTextUploadingField(null = True , blank = True)
    city = models.ForeignKey(City, verbose_name=("Select City"), on_delete=models.CASCADE,default="") 
    appointment_count = models.PositiveSmallIntegerField(("Count Apointment"),default=0,null = True , blank = True)
    count = models.PositiveSmallIntegerField(("Count For Appointment"),default=0)
    view = models.PositiveSmallIntegerField(("View Count"),default=0)
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        get_latest_by = 'created_at'

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, verbose_name=("Select User"), on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner,verbose_name=("Select Owner"), on_delete=models.CASCADE)
    fname = models.CharField(("Enter First Name"), max_length=50)
    lname = models.CharField(("Enter Last Name"), max_length=50)
    img = models.ImageField(("Insert Image"), upload_to="employee",null = True , blank = True)
    img_thumb = ImageSpecField(source='img',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 100})
    contact = models.PositiveIntegerField(null = True , blank = True)
    email = models.EmailField(max_length=254,default = "")
    # , height_field=None, width_field=None, max_length=None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name =("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.fname+" "+self.lname

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
