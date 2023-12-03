class ProcessorUnitInfo():
    def __init__(self):
        pass

    def is_processor_unit_ok(self, info):
        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'].lower() == 'ok':
            return True

        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'] == '':
            return True

        return False

    def get_processor_unit_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in ['Architecture', 'Model', 'NumCores', 'NumCoresEnabled', 'NumThreads', 'Pid', 'OperState', 'Presence', 'ProcessorId', 'SocketDesignation', 'Speed', 'Stepping', 'Vendor', 'Thermal']:
            info[key] = managed_object[key]

        if info['Presence'] == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        if info['OperState'] == 'operable':
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

        return info
