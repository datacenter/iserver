class CondHclStatusDetailInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'HardwareStatus',
            'HclCimcVersion',
            'HclDriverName',
            'HclDriverVersion',
            'HclFirmwareVersion',
            'HclModel',
            'Reason',
            'SoftwareStatus',
            'Status',
            'Moid'
        ]

        for key in keys:
            if key in managed_object:
                info[key] = managed_object[key]

        for key in ['Status', 'SoftwareStatus', 'HardwareStatus']:
            if key in info:
                if info[key] == 'Incomplete':
                    info['__Output'][key] = 'Red'

                if info[key] == 'Not-Listed':
                    info['__Output'][key] = 'Yellow'

                if info[key] == 'Validated':
                    info['__Output'][key] = 'Green'

                if info[key] == 'Not-Evaluated':
                    info['__Output'][key] = 'Yellow'

        return info
