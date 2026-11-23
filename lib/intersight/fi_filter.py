from lib import filter_helper


class FiFilter():
    def __init__(self):
        pass

    def moid_filter_match_mo(self, fi, moids):
        if fi['Moid'] in moids.split(','):
            return True
        return False

    def model_filter_match_mo(self, fi_mo, model_filter):
        for item in model_filter:
            if '*' in item:
                if filter_helper.match_string(item, fi_mo['Model']):
                    return True
            if '*' not in model_filter:
                if item.lower() in fi_mo['Model'].lower():
                    return True
        return False

    def serial_filter_match_mo(self, fi_mo, serials):
        for item in serials:
            if '*' in item:
                if filter_helper.match_string(item, fi_mo['Serial']):
                    return True
            if '*' not in item:
                if fi_mo['Serial'] == item:
                    return True
        return False

    def match_fi_mo(self, fi_mo, match_rules):
        if fi_mo['SwitchType'] != 'FabricInterconnect':
            return False

        if match_rules is None:
            return True

        if 'moid' in match_rules and len(match_rules['moid']) > 0:
            if not self.moid_filter_match_mo(fi_mo, match_rules['moid']):
                return False

        if 'model' in match_rules and len(match_rules['model']) > 0:
            if not self.model_filter_match_mo(fi_mo, match_rules['model']):
                return False

        if 'serial' in match_rules and len(match_rules['serial']) > 0:
            if not self.serial_filter_match_mo(fi_mo, match_rules['serial']):
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
