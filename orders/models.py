from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime    
from django.contrib.auth.models import User



# Create your models here.
class Location(models.Model):
    street = models.CharField(_("Strre"), max_length=250)
    city = models.CharField(_("City"), max_length=250)
    #constumer = models.ForeignKey(User, verbose_name=_("Constumer"), on_delete=models.CASCADE )
    
    def __str__(self):
        return self.street + self.city
    
class Order(models.Model):
    constumer = models.ForeignKey(User, verbose_name=_("Constumer"), on_delete=models.PROTECT )
    location = models.ForeignKey(Location, verbose_name=_("Location"), on_delete=models.PROTECT)
    postal_code = models.PositiveSmallIntegerField(_("Code Postal"), max_length=5)
    created_at = models.DateTimeField(_("Ordred at"), auto_now=False, auto_now_add=False, default=datetime.now())
    
    
class OrderLine(models.Model):
    food = models.ForeignKey("foods.Food", verbose_name=_("Ordred Food"), on_delete=models.PROTECT)
    quant = models.PositiveSmallIntegerField(_("Quantity"), max_length=2)
    order =  models.ForeignKey(Order, related_name='order_of_line', on_delete=models.PROTECT)
    
    @property
    def price_ol(self):
        return self.quant * self.food.price