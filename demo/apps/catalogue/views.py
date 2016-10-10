from django.utils.translation import ugettext as _
from django.views.generic import ListView

from oscar.apps.catalogue.views import (
    ProductDetailView as CoreProductDetailView
    )
from oscar.core.loading import get_model, get_class


Product = get_model('catalogue', 'product')
Manufacturer = get_model('catalogue', 'Manufacturer')

class ProductDetailView(CoreProductDetailView):
    """
    Show product detail view
    """
    def get_context_data(self, **kwargs):
        ctx = super(ProductDetailView, self).get_context_data(**kwargs)
        ctx['manufacturer'] = self.object.manufacturer
        return ctx


class ManufacturersListView(ListView):
    """
    Browse all manufacturers
    """
    model = Manufacturer
    template_name = 'flatpages/manufacturers.html'
    title = _('Manufacturers')

    def get_context_data(self, **kwargs):
        ctx = super(ManufacturersListView, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx
