from django.db import models
from django.utils.translation import ugettext as _

from oscar.apps.catalogue.abstract_models import (
	AbstractProduct as CoreProduct
	)


class Product(CoreProduct):
	manufacturer = models.ForeignKey(
									 'Manufacturer',
									 verbose_name=_('Manufacturer')
									 )


class Manufacturer(models.Model):
    name = models.CharField(
                            max_length=128, 
                            verbose_name=_('Name')
                            )
    image = models.ImageField(
                              verbose_name=_('Image'),
                              upload_to='manufacturers', blank=True,
                              null=True, max_length=255
                              )
    description = models.TextField(
                                   blank=True, 
                                   verbose_name=_('Description')
                                   )

    class Meta():
        app_label = 'catalogue'
        ordering = ['name']
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')

    def __str__(self):
        return self.name
		

from oscar.apps.catalogue.models import *  # noqa
