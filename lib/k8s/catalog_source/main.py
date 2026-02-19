from lib.k8s.catalog_source.api import K8sCatalogSourceApi
from lib.k8s.catalog_source.info import K8sCatalogSourceInfo


class K8sCatalogSource(
        K8sCatalogSourceApi,
        K8sCatalogSourceInfo
        ):
    def __init__(self):
        K8sCatalogSourceApi.__init__(self)
        K8sCatalogSourceInfo.__init__(self)
