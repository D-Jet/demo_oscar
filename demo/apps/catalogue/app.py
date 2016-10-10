from django.conf.urls import url, include

from oscar.core.application import Application
from oscar.core.loading import get_class
from oscar.apps.catalogue.app import (
    BaseCatalogueApplication as CoreBaseCatalogueApplication,
    ReviewsApplication
    )

from .views import (
    ManufacturersListView,
    )


class BaseCatalogueApplication(CoreBaseCatalogueApplication):
    makers_view = ManufacturersListView

    def get_urls(self):
        urlpatterns = super(BaseCatalogueApplication, self).get_urls()
        urlpatterns += [
                        url(r'^makers/$', self.makers_view.as_view(), name='makers'),
                        ]
        return self.post_process_urls(urlpatterns)
        

class CatalogueApplication(BaseCatalogueApplication, ReviewsApplication):
    """
    Composite class combining Products with Reviews
    """


application = CatalogueApplication()