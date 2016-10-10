from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from django_tables2 import SingleTableMixin

from oscar.apps.dashboard.catalogue.views import (
    ProductCreateUpdateView as CoreProductCreateUpdateView
    )
from oscar.core.loading import get_classes, get_model
from oscar.views.generic import ObjectLookupView

from .forms import (
    ManufacturerForm
    )


Manufacturer = get_model('catalogue', 'Manufacturer')


class ManufacturerCreateUpdateView(generic.UpdateView):

    template_name = 'dashboard/catalogue/manufacturer_form.html'
    model = Manufacturer
    form_class = ManufacturerForm

    def process_all_forms(self, form):
        """
        This validates the Manufacturer form
        making it possible to display all errors at once.
        """
        if self.creating and form.is_valid():
            self.object = form.save(commit=False)

        is_valid = form.is_valid()

        if is_valid:
            return self.forms_valid(form)
        else:
            return self.forms_invalid(form)

    def forms_valid(self, form):
        form.save()

        return HttpResponseRedirect(self.get_success_url())

    def forms_invalid(self, form):
        messages.error(self.request,
                       _("Your submitted data was not valid - please "
                         "correct the errors below"
                         ))
        ctx = self.get_context_data(form=form)
        return self.render_to_response(ctx)

    form_valid = form_invalid = process_all_forms

    def get_context_data(self, *args, **kwargs):
        ctx = super(ManufacturerCreateUpdateView, self).get_context_data(
            *args, **kwargs)

        ctx["title"] = self.get_title()

        return ctx


class ManufacturerCreateView(ManufacturerCreateUpdateView):

    creating = True

    def get_object(self):
        return None

    def get_title(self):
        return _("Add new manufacturer")

    def get_success_url(self):
        messages.info(self.request, _("Manufacturer added successfully"))
        return reverse("dashboard:catalogue-manufacturer-list")


class ManufacturerUpdateView(ManufacturerCreateUpdateView):

    creating = False

    def get_title(self):
        return _("Update manufacturer '%s'") % self.object.name

    def get_success_url(self):
        messages.info(self.request, _("Manufacturer updated successfully"))
        return reverse("dashboard:catalogue-manufacturer-list")

    def get_object(self):
        manufacturer = get_object_or_404(Manufacturer, pk=self.kwargs['pk'])
        return manufacturer


class ManufacturerListView(generic.ListView):
    template_name = 'dashboard/catalogue/manufacturer_list.html'
    context_object_name = 'manufacturers'
    model = Manufacturer

    def get_context_data(self, *args, **kwargs):
        ctx = super(ManufacturerListView, self).get_context_data(*args,
                                                                 **kwargs)
        ctx['title'] = _("Manufacturers")
        return ctx


class ManufacturerDeleteView(generic.DeleteView):
    template_name = 'dashboard/catalogue/manufacturer_delete.html'
    model = Manufacturer
    form_class = ManufacturerForm

    def get_context_data(self, *args, **kwargs):
        ctx = super(ManufacturerDeleteView, self).get_context_data(*args,
                                                                   **kwargs)
        ctx['title'] = _("Remove manufacturer '%s'") % self.object.name

        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Manufacturer removed successfully"))
        return reverse("dashboard:catalogue-manufacturer-list")
