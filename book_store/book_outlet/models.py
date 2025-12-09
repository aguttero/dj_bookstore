from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
# check django docs for field types

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"ISO: {self.code}, {self.name}"
    
    class Meta:
        verbose_name_plural = "Country Entries"   

    # en shell se usa method .add para agregar items a la relacion many to many
    # book_object_var.published_countries.add(<country name>)
    # El reverse connection es <table>_set
    # country = Country.objects.all()[0]
    # country.book_set.all()


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

      # override default __str__() method:
    def __str__(self):
        return f"zip:{self.postal_code}, {self.city}"

    #to add additional settings for display or other purposes that don't affect the DataBase. Este ejemplo cambia el 'Adressesssss' en el admin console

    class Meta:
        verbose_name = "Address_en_singular"
        verbose_name_plural = "Address Entries"        


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

      # override default __str__() method:
    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # V01 author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    # revisar las opciones de SETNULL y PROTECT
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # slug = models.SlugField(default="", blank=True, editable=False, null=False, db_index=True)
    #editable = False Oculta el campo del admin page
    #blank=True permite que un submit desde form lo deje en blanco (a pesar del null = false)
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book_slug_url", args=[self.slug])
    
    # override default save() method to autopopulate slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    # override default __str__() method:
    def __str__(self):
        return f"{self.title}({self.rating})"
