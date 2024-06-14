from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.workflow.info import WorkflowInfo


class Workflow(IntersightCommon, WorkflowInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'workflow workflowinfo'
        self.cache_key = 'workflow'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id, cache_key=self.cache_key)
        WorkflowInfo.__init__(self)
