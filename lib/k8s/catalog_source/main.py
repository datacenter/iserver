from lib.k8s.catalog_source.api import K8sCatalogSourceApi
from lib.k8s.catalog_source.info import K8sCatalogSourceInfo
from lib.k8s.catalog_source.create import K8sCatalogSourceCreate
from lib.k8s.catalog_source.delete import K8sCatalogSourceDelete
from lib.k8s.catalog_source.wait import K8sCatalogSourceWait


class K8sCatalogSource(
        K8sCatalogSourceApi,
        K8sCatalogSourceInfo,
        K8sCatalogSourceCreate,
        K8sCatalogSourceDelete,
        K8sCatalogSourceWait
        ):
    def __init__(self):
        K8sCatalogSourceApi.__init__(self)
        K8sCatalogSourceInfo.__init__(self)
        K8sCatalogSourceCreate.__init__(self)
        K8sCatalogSourceDelete.__init__(self)
        K8sCatalogSourceWait.__init__(self)
