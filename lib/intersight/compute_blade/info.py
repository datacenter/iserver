class ComputeBladeInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Dn',
            'HardwareUuid',
            'Model',
            'Moid',
            'Name',
            'NumAdaptors',
            'NumCpuCores',
            'NumCpuCoresEnabled',
            'NumCpus',
            'NumEthHostInterfaces',
            'NumFcHostInterfaces',
            'NumThreads',
            'OperPowerState',
            'Pid',
            'Presence',
            'Serial',
            'ServiceProfile',
            'SlotId',
            'TotalMemory',
            'Vendor'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['Pid'] is None or len(info['Pid']) == 0:
            info['Pid'] = info['Model']

        info['ServerName'] = 'Server #%s' % (
            managed_object['SlotId']
        )

        info['AlarmCritical'] = managed_object['AlarmSummary']['Critical']
        info['AlarmWarning'] = managed_object['AlarmSummary']['Warning']
        if managed_object['AlarmSummary']['Warning'] == 0 and managed_object['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Healthy'
            info['HealthSummary'] = 'Healthy'
            info['__Output']['Health'] = 'Green'
            info['__Output']['HealthSummary'] = 'Green'
        if managed_object['AlarmSummary']['Warning'] > 0 and managed_object['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Warnings'
            info['HealthSummary'] = 'Warnings (%s)' % (managed_object['AlarmSummary']['Warning'])
            info['__Output']['Health'] = 'Yellow'
            info['__Output']['HealthSummary'] = 'Yellow'
        if managed_object['AlarmSummary']['Critical'] > 0:
            info['Health'] = 'Critical'
            info['HealthSummary'] = 'Critical (%s)' % (managed_object['AlarmSummary']['Critical'])
            info['__Output']['Health'] = 'Red'
            info['__Output']['HealthSummary'] = 'Red'

        info['PowerOn'] = False
        if managed_object['OperPowerState'] == 'on':
            info['PowerOn'] = True
            info['__Output']['OperPowerState'] = 'Green'
        else:
            info['__Output']['OperPowerState'] = 'Red'

        info['CpuSummary'] = '%sS %sC %sT' % (
            info['NumCpus'],
            info['NumCpuCores'],
            info['NumThreads']
        )
        info['TotalMemoryUnit'] = self.info_helper.convert_memory(
            info['TotalMemory'] * 1024 * 1024
        )

        return info
