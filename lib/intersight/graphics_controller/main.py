from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.graphics_controller.info import GraphicsControllerInfo


class GraphicsController(IntersightCommon, GraphicsControllerInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'graphics controller'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        GraphicsControllerInfo.__init__(self)
