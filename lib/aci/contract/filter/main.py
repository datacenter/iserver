from lib.aci.contract.filter.api import FilterApi
from lib.aci.contract.filter.info import FilterInfo


class Filter(FilterApi, FilterInfo):
    def __init__(self):
        FilterApi.__init__(self)
        FilterInfo.__init__(self)
