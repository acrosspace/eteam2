from django.db import models

# Create your models here.

# django.db.models.Model is the base class for all models in Django
# Fields are defined as class attributes on the model, with each field representing a column in the database table.
# Each field is an instance of the Field class, which is used to specify the type of data each field holds.
# Records are represented as instances of the model, and each instance of the model represents a row in the database table.
class Hello(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    contact_email = models.EmailField()
    is_active = models.BooleanField()
    def __str__(self):
        return self.name