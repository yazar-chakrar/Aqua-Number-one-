import datetime
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Review(models.Model):
    food = models.ForeignKey("foods.Food", verbose_name=_("Food : "), on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(_("Nom de personne"), max_length=255) 
    discription = models.CharField(_("Review"))
    date = models.DateField(_("date"), auto_now_add=True)
