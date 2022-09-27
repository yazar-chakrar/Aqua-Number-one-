from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime    
from django.contrib.auth.models import User



# Create your models here.
      
    
class Order(models.Model):
    constumer = models.ForeignKey(User, verbose_name=_("Constumer"), on_delete=models.CASCADE )
    #constumer = models.ForeignKey("User.Model", verbose_name=_("constumer"), on_delete=models.CASCADE)
    location = models.CharField(_("Location"), max_length=50)
    postal_code = models.CharField(_("Code Postal"), max_length=5)
    created_at = models.DateTimeField(_("Ordred at"), auto_now=False, auto_now_add=False, default=datetime.now())
    
    
class OrderLine(models.Model):
    food = models.ForeignKey("foods.Food", verbose_name=_("Ordred Food"), on_delete=models.CASCADE)
    quant = models.IntegerField(_("Quqntity"))
    order =  models.ForeignKey(Order, related_name='order_of_line', on_delete=models.CASCADE)
    
    @property
    def price_ol(self):
        return self.quant * self.food.price