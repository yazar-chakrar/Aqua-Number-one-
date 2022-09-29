from email.policy import default
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from datetime import datetime    
from django.contrib.auth.models import User

# Create your models here.

class BookCategory(MPTTModel):
    title = models.CharField(_("Book Category"), max_length=200)
    slug = models.CharField(_("Book Category slug"), max_length=200)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, unique=False, blank=True, related_name='children')
    
    def __str__(self):
        return self.title

class Book(models.Model):
    constumer = models.ForeignKey(User, verbose_name=_("Constumer"), on_delete=models.CASCADE )
    category = models.ForeignKey(BookCategory, verbose_name=_("Book Category"), on_delete=models.CASCADE, default=0)
    booking_date = models.DateTimeField(_("Booking Time"), auto_now=False, auto_now_add=False)
    duration = models.DurationField(_("Booking duration"))
    persons = models.IntegerField(_("Number of persens"), max_length=2, default=1)
    
    def __str__(self):
        return str(self.category) + '/' + str(self.constumer) + '/'+ str(self.booking_date)