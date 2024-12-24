from django.db import models


class icecream(models.Model):
    name = models.CharField(max_length=100)
    taste = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5,decimal_places=2 )

    def __str__ (self):
     return (f'{self.name} - ({self.cost})')

class iceshop(models.Model):
    name = models.CharField(max_length=100)
    ice_cream = models.ManyToManyField(icecream)
    def __str__ (self):
     return (f'{self.name} ')

#   models.ForeignKey(Parent) !!!!!!!!  один ко многим

class Parent(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.lastname}'

class Children(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return f'{self.name} {self.lastname}, age: {self.age}'
