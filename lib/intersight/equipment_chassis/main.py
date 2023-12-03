from lib.intersight.intersight_common import IntersightCommon


class EquipmentChassis(IntersightCommon):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment chassis'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def filter(self, name_filter='', serial_filter='', model_filter=''):
        items = IntersightCommon.get_all(self)
        if items is None:
            return None

        if len(name_filter) == 0 and len(serial_filter) == 0 and len(model_filter) == 0:
            return items

        filtered = []
        for item in items:
            if len(name_filter) > 0 and name_filter.lower() not in item['Name'].lower():
                continue

            if len(serial_filter) > 0:
                found = False
                for item_filter in serial_filter.split(','):
                    if item_filter.lower() in item['Serial'].lower():
                        found = True

                if not found:
                    continue

            if len(model_filter) > 0 and model_filter.lower() not in item['Model'].lower():
                continue

            filtered.append(item)

        return filtered
