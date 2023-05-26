from lib.aci.contract.taboo_subject.api import TabooSubjectApi
from lib.aci.contract.taboo_subject.info import TabooSubjectInfo


class TabooSubject(TabooSubjectApi, TabooSubjectInfo):
    def __init__(self):
        TabooSubjectApi.__init__(self)
        TabooSubjectInfo.__init__(self)
