from lib.intersight.intersight_common import IntersightCommon


class MemoryUnit(IntersightCommon):
    """Class for intersight memory unit led objects
    {
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "AdminState": "policy",
    "Ancestors": [
        {
        "ClassId": "mo.MoRef",
        "Moid": "6311ac8376752d31398e5c4d",
        "ObjectType": "memory.Array",
        "link": "https://www.intersight.com/api/v1/memory/Arrays/6311ac8376752d31398e5c4d"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "6311ac4676752d31398e5331",
        "ObjectType": "compute.Board",
        "link": "https://www.intersight.com/api/v1/compute/Boards/6311ac4676752d31398e5331"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "6311aae876752d31398e1a50",
        "ObjectType": "compute.RackUnit",
        "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
        }
    ],
    "ArrayId": 1,
    "Bank": 1,
    "Capacity": "16384",
    "ClassId": "memory.Unit",
    "Clock": "2400",
    "CreateTime": "2022-09-02T07:10:59.81Z",
    "DeviceMoId": "61c35fa36f72612d3005590c",
    "DisplayNames": {
        "hierarchical": [
        "memory-unit-DIMM_H3"
        ],
        "short": [
        "Memory-DIMM_H3"
        ]
    },
    "Dn": "sys/rack-unit-3/board/memarray-1/mem-24",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "FormFactor": "DIMM",
    "InventoryDeviceInfo": null,
    "Latency": "0.400000",
    "Location": "DIMM_H3",
    "MemoryArray": {
        "ClassId": "mo.MoRef",
        "Moid": "6311ac8376752d31398e5c4d",
        "ObjectType": "memory.Array",
        "link": "https://www.intersight.com/api/v1/memory/Arrays/6311ac8376752d31398e5c4d"
    },
    "MemoryId": 24,
    "ModTime": "2022-09-02T07:18:38.404Z",
    "Model": "M393A2K40BB1-CRC",
    "Moid": "6311ac8376752d31398e5c7d",
    "ObjectType": "memory.Unit",
    "OperPowerState": "not-supported",
    "OperReason": [],
    "OperState": "operable",
    "Operability": "unknown",
    "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "61c35fa36f72612d3005590c"
    ],
    "Parent": {
        "ClassId": "mo.MoRef",
        "Moid": "6311ac8376752d31398e5c4d",
        "ObjectType": "memory.Array",
        "link": "https://www.intersight.com/api/v1/memory/Arrays/6311ac8376752d31398e5c4d"
    },
    "PermissionResources": [
        {
        "ClassId": "mo.MoRef",
        "Moid": "5dee1d736972652d321d26b5",
        "ObjectType": "organization.Organization",
        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "625706a06972652d3202a8f9",
        "ObjectType": "organization.Organization",
        "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "6242d1016972652d32eda017",
        "ObjectType": "organization.Organization",
        "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
        }
    ],
    "Presence": "equipped",
    "PreviousFru": null,
    "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "61c35fa36f72612d3005590c",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
    },
    "Revision": "0",
    "Rn": "",
    "Serial": "322E755D",
    "Set": 0,
    "SharedScope": "",
    "Speed": "unspecified",
    "Tags": [],
    "Thermal": "ok",
    "Type": "DDR4",
    "Vendor": "0xCE00",
    "Visibility": "yes",
    "Width": "64"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'memory unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def is_memory_unit_ok(self, info):
        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'] == 'ok':
            return True

        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'] == '':
            return True

        return False

    def get_memory_units_info(self):
        memory_units = self.get_all()
        if memory_units is None:
            return None

        memory_units_info = []
        for memory_unit in memory_units:
            info = {}
            info['__Output'] = {}

            for key in ['ArrayId', 'Bank', 'Capacity', 'Clock', 'Dn', 'FormFactor', 'Latency', 'Location', 'MemoryId', 'Model', 'OperState', 'Presence', 'Serial', 'Speed', 'Thermal', 'Type', 'Vendor']:
                info[key] = memory_unit[key]

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
            for ancestor in memory_unit['Ancestors']:
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

            if self.is_memory_unit_ok(info):
                info['StateTick'] = '\u2713'
                info['__Output']['StateTick'] = 'Green'
            else:
                info['StateTick'] = '\u2717'
                info['__Output']['StateTick'] = 'Red'

            memory_units_info.append(info)

        memory_units_info = sorted(memory_units_info, key=lambda i: int(i['MemoryId']))

        return memory_units_info
