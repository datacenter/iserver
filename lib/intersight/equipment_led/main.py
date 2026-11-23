from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.equipment_led.info import EquipmentLedInfo


class EquipmentLed(IntersightCommon, EquipmentLedInfo):
    def __init__(self, iaccount, get_filter='"OperState eq \'on\'"', log_id=None):
        self.iobject = 'equipment locatorled'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        EquipmentLedInfo.__init__(self)
