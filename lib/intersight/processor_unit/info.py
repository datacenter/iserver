class ProcessorUnitInfo():
    def __init__(self):
        pass

    def is_processor_unit_ok(self, info):
        if info['OperState'].lower() not in ['operable', 'ok']:
            return False

        if info['Presence'].lower() not in ['equipped']:
            return False

        if info['Thermal'].lower() not in ['ok', '']:
            return False

        return True

    def get_processor_unit_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Architecture',
            'Model',
            'NumCores',
            'NumCoresEnabled',
            'NumThreads',
            'Pid',
            'OperState',
            'Presence',
            'ProcessorId',
            'SocketDesignation',
            'Speed',
            'Stepping',
            'Vendor',
            'Thermal'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['Presence'] == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        if info['OperState'].lower() in ['operable', 'ok']:
            info['__Output']['OperState'] = 'Green'
        else:
            info['__Output']['OperState'] = 'Red'

        if len(info['Thermal']) > 0:
            if info['Thermal'].lower() == 'ok':
                info['__Output']['Thermal'] = 'Green'
            else:
                info['__Output']['Thermal'] = 'Red'

        if self.is_processor_unit_ok(info):
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        info['VendorName'] = 'unknown'
        if info['Vendor'] is not None:
            if info['Vendor'].startswith('Intel'):
                info['VendorName'] = 'intel'
            if info['Vendor'].startswith('Advanced Micro Devices'):
                info['VendorName'] = 'amd'

        return info
