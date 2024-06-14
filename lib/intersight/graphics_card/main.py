from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.graphics_card.info import GraphicsCardInfo


class GraphicsCard(IntersightCommon, GraphicsCardInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'graphics card'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        GraphicsCardInfo.__init__(self)
