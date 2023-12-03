from lib import filter_helper


class ChassisFilter():
    def __init__(self):
        pass

    def moid_filter_match_mo(self, chassis, moids):
        if chassis['Moid'] in moids.split(','):
            return True
        return False

    def name_filter_match_mo(self, chassis_mo, name_filter):
        for item in name_filter:
            if '*' in item:
                if filter_helper.match_string(item, chassis_mo['Name']):
                    return True
            if '*' not in item:
                if item.lower() in chassis_mo['Name'].lower():
                    return True
        return False

    def model_filter_match_mo(self, chassis_mo, model_filter):
        for item in model_filter:
            if '*' in item:
                if filter_helper.match_string(item, chassis_mo['Model']):
                    return True
            if '*' not in model_filter:
                if item.lower() in chassis_mo['Model'].lower():
                    return True
        return False

    def serial_filter_match_mo(self, chassis_mo, serials):
        for item in serials:
            if '*' in item:
                if filter_helper.match_string(item, chassis_mo['Serial']):
                    return True
            if '*' not in item:
                if chassis_mo['Serial'] == item:
                    return True
        return False

    def match_chassis_mo(self, chassis_mo, match_rules):
        if match_rules is None:
            return True

        if 'moid' in match_rules and len(match_rules['moid']) > 0:
            if not self.moid_filter_match_mo(chassis_mo, match_rules['moid']):
                return False

        if 'name' in match_rules and len(match_rules['name']) > 0:
            if not self.name_filter_match_mo(chassis_mo, match_rules['name']):
                return False

        if 'model' in match_rules and len(match_rules['model']) > 0:
            if not self.model_filter_match_mo(chassis_mo, match_rules['model']):
                return False

        if 'serial' in match_rules and len(match_rules['serial']) > 0:
            if not self.serial_filter_match_mo(chassis_mo, match_rules['serial']):
                return False

        return True

    def get_mo_match_rules(self, moid_filter=None, name_filter=None, serial_filter=None, model_filter=None):
        match_rules = {}
        match_rules['moid'] = []
        match_rules['name'] = []
        match_rules['serial'] = []
        match_rules['model'] = []

        if moid_filter is not None and len(moid_filter) > 0:
            match_rules['moid'] = moid_filter

        if name_filter is not None and len(name_filter) > 0:
            match_rules['name'] = name_filter

        if serial_filter is not None and len(serial_filter) > 0:
            match_rules['serial'] = serial_filter

        if model_filter is not None and len(model_filter) > 0:
            match_rules['model'] = model_filter

        return match_rules
