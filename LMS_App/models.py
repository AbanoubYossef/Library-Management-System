from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):

    status_of_books =[
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
        
    ]

    title = models.CharField( max_length=250)
    author = models.CharField( max_length=250)
    photo_of_book = models.ImageField(upload_to='photos', null = True, blank =True)
    photo_of_author = models.ImageField(upload_to='photos', null = True, blank =True)
    pages_number = models.IntegerField(null = True, blank =True)
    price = models.DecimalField( max_digits=5, decimal_places=2, null = True, blank =True)
    rental_per_day_price = models.DecimalField( max_digits=5, decimal_places=2, null = True, blank =True)
    Toatal_rental = models.DecimalField( max_digits=5, decimal_places=2, null = True, blank =True)
    rental_period = models.IntegerField(null = True, blank = True)
    active = models.BooleanField(default = True)
    status = models.CharField( max_length=250, choices = status_of_books, null = True, blank =True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null = True, blank =True)


    def __str__(self):
        return self.title
    