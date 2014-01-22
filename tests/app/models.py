from django.db import models

from django_dynamic_finder.managers import DynamicFinderManager

class Product(models.Model):
    name = models.CharField(max_length=50)
    
    objects = DynamicFinderManager()

    class Meta:
        verbose_name = 'Product'

    def __unicode__(self):
        return "#%s - %s" % (self.pk, self.name)