from multiprocessing import parent_process
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from datetime import datetime    



# Create your models here.

class Category(MPTTModel):
    title = models.CharField(_("Category"), max_length=200)
    slug = models.CharField(_("Category slug"), max_length=200)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, unique=False, blank=True, related_name='children')
    
    def __str__(self):
        return self.title

class Food(models.Model):
    category = models.ForeignKey( Category, on_delete=models.CASCADE, default=0)
    title = models.CharField(_("Food Price"), max_length=200)
    disc = models.CharField(_("Food Price"), max_length=200)
    image = models.ImageField(_("Food Image"), upload_to='foods/', height_field=None, width_field=None, max_length=None, default='default/default-food.jpg')
    slug = models.CharField(_("Food slug"), max_length=200)
    price = models.FloatField(_("Food Price"))
    old_price = models.FloatField(_("Food Price"))
    is_avaible = models.BooleanField(_("Food Avaible"))
    created_at = models.DateTimeField(_("Food Created at"), auto_now=False, auto_now_add=False, default=datetime.now())
    
    def __str__(self):
        return self.title
