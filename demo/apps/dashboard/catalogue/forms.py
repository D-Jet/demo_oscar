from decimal import Decimal

from django import forms
from django.core import exceptions
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from treebeard.forms import movenodeform_factory

from oscar.apps.dashboard.catalogue.forms import (
    ProductForm as CoreProductForm,
    )
from oscar.core.loading import get_class, get_model
from oscar.core.utils import slugify
from oscar.forms.widgets import ImageInput


Manufacturer = get_model('catalogue', 'Manufacturer')
Product = get_model('catalogue', 'Product')


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Manufacturer
        fields = ['name', 'image', 'description']

        widgets = {
            'image': ImageInput(),
        }


def _attr_text_field(attribute):
    return forms.CharField(label=attribute.name,
                           required=attribute.required)


def _attr_textarea_field(attribute):
    return forms.CharField(label=attribute.name,
                           widget=forms.Textarea(),
                           required=attribute.required)


def _attr_integer_field(attribute):
    return forms.IntegerField(label=attribute.name,
                              required=attribute.required)


def _attr_boolean_field(attribute):
    return forms.BooleanField(label=attribute.name,
                              required=attribute.required)


def _attr_float_field(attribute):
    return forms.FloatField(label=attribute.name,
                            required=attribute.required)


def _attr_date_field(attribute):
    return forms.DateField(label=attribute.name,
                           required=attribute.required,
                           widget=forms.widgets.DateInput)

class ProductForm(CoreProductForm):

    FIELD_FACTORIES = {
        "text": _attr_text_field,
        "richtext": _attr_textarea_field,
        "integer": _attr_integer_field,
        "boolean": _attr_boolean_field,
        "float": _attr_float_field,
        "date": _attr_date_field,
    }

    class Meta:
        model = Product
        fields = [
            'title', 'upc', 'manufacturer', 'description', 'is_discountable']
