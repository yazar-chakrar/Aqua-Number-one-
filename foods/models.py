from multiprocessing import parent_process
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _
from datetime import datetime    
from django.utils.text import slugify



# Create your models here.

class Category(MPTTModel):
    title = models.CharField(_("Category"), max_length=50)
    slug = models.CharField(_("Category slug"), max_length=60)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, unique=False, blank=True, related_name='children')
    
    def __str__(self):
        return self.title

class Food(models.Model):
    ''' web_id = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product website ID"),
        help_text=_("format: required, unique"),
    ) '''
    category = models.ForeignKey( Category, on_delete=models.CASCADE, default=0)
    title = models.CharField(_("Food title"), max_length=20)
    disc = models.CharField(_("Food disc"), max_length=200)
    image = models.ImageField(_("Food Image"), upload_to='foods/', height_field=None, width_field=None, max_length=None, default='default/default-food.jpg')
    price = models.FloatField(_("Food Price"))
    old_price = models.FloatField(_("Food Price"))
    is_avaible = models.BooleanField(_("Food Avaible"))
    created_at = models.DateTimeField(_("Food Created at"), auto_now=False, auto_now_add=False, default=datetime.now())
    
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.title)
        super(Food, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
