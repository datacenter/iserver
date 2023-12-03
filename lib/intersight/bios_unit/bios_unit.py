from lib.intersight.intersight_common import IntersightCommon


class BiosUnit(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'bios unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
