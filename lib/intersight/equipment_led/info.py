class EquipmentLedInfo():
    def __init__(self):
        pass

    def is_locator_led_on(self, managed_object):
        if managed_object is None or 'OperState' not in managed_object or managed_object['OperState'] is None:
            return False
        if managed_object['OperState'].lower() == 'off':
            return False
        return True
