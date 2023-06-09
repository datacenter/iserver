from lib.intersight.intersight_common import IntersightCommon


class ProcessorUnit(IntersightCommon):
    """Class for intersight processor unit objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed96176752d32d52214",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/5e8c4ed96176752d32d52214"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed26176752d32d51c40",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5e8c4ed26176752d32d51c40"
        }
        ],
        "Architecture": "Xeon",
        "ClassId": "processor.Unit",
        "ComputeBlade": null,
        "ComputeBoard": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed96176752d32d52214",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/5e8c4ed96176752d32d52214"
        },
        "ComputeRackUnit": null,
        "CreateTime": "2020-04-07T10:03:24.112Z",
        "DeviceMoId": "5e8c4ecd6f72612d302b11a6",
        "Dn": "sys/rack-unit-1/board/cpu-2",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "InventoryDeviceInfo": null,
        "ModTime": "2022-05-09T13:36:01.136Z",
        "Model": "Intel(R) Xeon(R) CPU E5-2630 v3 @ 2.40GHz",
        "Moid": "5e8c4fec6176752d32d62da8",
        "NetworkElement": null,
        "NumCores": 8,
        "NumCoresEnabled": "8",
        "NumThreads": "16",
        "ObjectType": "processor.Unit",
        "OperPowerState": "",
        "OperReason": [],
        "OperState": "operable",
        "Operability": "",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5e8c4ecd6f72612d302b11a6"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed96176752d32d52214",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/5e8c4ed96176752d32d52214"
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
        "ProcessorId": 2,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ecd6f72612d302b11a6",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5e8c4ecd6f72612d302b11a6"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "",
        "SharedScope": "",
        "SocketDesignation": "CPU2",
        "Speed": 2.4,
        "Stepping": "2",
        "Tags": [],
        "Thermal": "",
        "Vendor": "Intel(R) Corporation"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'processor unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def is_processor_unit_ok(self, info):
        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'].lower() == 'ok':
            return True

        if info['OperState'] == 'operable' and info['Presence'] == 'equipped' and info['Thermal'] == '':
            return True

        return False

    def get_processor_units_info(self):
        processor_units = self.get_all()
        if processor_units is None:
            return None

        processor_units_info = []
        for processor_unit in processor_units:
            info = {}
            info['__Output'] = {}
            for key in ['Architecture', 'Model', 'NumCores', 'NumCoresEnabled', 'NumThreads', 'OperState', 'Presence', 'ProcessorId', 'SocketDesignation', 'Speed', 'Stepping', 'Vendor', 'Thermal']:
                info[key] = processor_unit[key]

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

            processor_units_info.append(info)

        processor_units_info = sorted(
            processor_units_info,
            key=lambda i: i['ProcessorId']
        )

        return processor_units_info
