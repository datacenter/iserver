class ChassisFilter():
    def __init__(self):
        pass

    def name_filter_match_mo(self, chassis_mo, name_filter):
        for item in name_filter:
            if item.lower() in chassis_mo['Name'].lower():
                return True
        return False

    def model_filter_match_mo(self, chassis, model_filter):
        for item in model_filter:
            if item.lower() in chassis['Model'].lower():
                return True
        return False

    def serial_filter_match_mo(self, chassis, serials):
        if chassis['Serial'] in serials:
            return True
        return False

    def match_chassis_mo(self, chassis_mo, match_rules):
        if match_rules is None:
            return True

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

    def get_mo_match_rules(self, name_filter=None, serial_filter=None, model_filter=None):
        match_rules = {}
        match_rules['name'] = []
        match_rules['serial'] = []
        match_rules['model'] = []

        if name_filter is not None and len(name_filter) > 0:
            match_rules['name'] = name_filter

        if serial_filter is not None and len(serial_filter) > 0:
            match_rules['serial'] = serial_filter

        if model_filter is not None and len(model_filter) > 0:
            match_rules['model'] = model_filter

        return match_rules
