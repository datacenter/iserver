from lib.aci.contract.subject.api import SubjectApi
from lib.aci.contract.subject.info import SubjectInfo


class Subject(SubjectApi, SubjectInfo):
    def __init__(self):
        SubjectApi.__init__(self)
        SubjectInfo.__init__(self)
