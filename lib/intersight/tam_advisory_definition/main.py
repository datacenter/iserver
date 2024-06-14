from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.tam_advisory_definition.info import TamAdvisoryDefinitionInfo


class TamAdvisoryDefinition(IntersightCommon, TamAdvisoryDefinitionInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'tam advisorydefinition'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        TamAdvisoryDefinitionInfo.__init__(self)
