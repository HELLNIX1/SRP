from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu/")
    price = models.DecimalField(max_digits=4,decimal_places=2)
    category = models.ManyToManyField('Category',related_name = 'item')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Orderr(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    items = models.ManyToManyField('MenuItem',related_name= 'order',blank = True)
    name = models.CharField(max_length=50, blank=True)
    is_paid = models.BooleanField(default=False)
    ordergiven = models.BooleanField(default=False)
    def __str__(self):
      
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
     


