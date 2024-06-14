class MemoryUnitInfo():
    def __init__(self):
        pass

    def is_memory_unit_ok(self, info):
        if info['OperState'].lower() not in ['operable', 'ok']:
            return False

        if info['Presence'].lower() not in ['equipped']:
            return False

        if info['Thermal'].lower() not in ['ok', '']:
            return False

        return True

    def get_memory_unit_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'ArrayId',
            'Bank',
            'Capacity',
            'Clock',
            'Description',
            'Dn',
            'FormFactor',
            'Latency',
            'Location',
            'MemoryId',
            'Model',
            'OperState',
            'Pid',
            'Presence',
            'Serial',
            'Speed',
            'Thermal',
            'Type',
            'Vendor'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['LatencyUnit'] = ''
        if info['Latency'] not in ['unspecified', '']:
            info['LatencyUnit'] = '%s ns' % (
                round(
                    float(info['Latency']),
                    2
                )
            )

        info['CapacityUnit'] = ''
        if info['Capacity'] != 'unspecified':
            info['CapacityUnit'] = self.info_helper.convert_memory(
                int(info['Capacity']) * 1024 * 1024,
                precision=0
            )

        info['MemoryArrayId'] = None
        info['ChassisId'] = None
        info['ServerId'] = None
        info['BoardId'] = None
        for ancestor in managed_object['Ancestors']:
            if ancestor['ObjectType'] == 'memory.Array':
                info['MemoryArrayId'] = ancestor['Moid']
            if ancestor['ObjectType'] == 'compute.Board':
                info['BoardId'] = ancestor['Moid']
            if ancestor['ObjectType'] == 'equipment.Chassis':
                info['ChassisId'] = ancestor['Moid']
            if ancestor['ObjectType'] == 'compute.Blade':
                info['ServerId'] = ancestor['Moid']
            if ancestor['ObjectType'] == 'compute.RackUnit':
                info['ServerId'] = ancestor['Moid']

        if info['Presence'].lower() in ['equipped']:
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

        if self.is_memory_unit_ok(info):
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        return info
