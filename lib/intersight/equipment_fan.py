from lib.intersight.intersight_common import IntersightCommon


class EquipmentFan(IntersightCommon):
    """Class for intersight equipment fan objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b576752d3236304d17",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d17"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "ClassId": "equipment.Fan",
        "CreateTime": "2022-09-21T13:46:29.627Z",
        "Description": "Fan Module for UCSX 9508 Blade Server Chassis",
        "DeviceMoId": "632999466f72612d39b26942",
        "DisplayNames": {
            "hierarchical": [
                "fan-1"
            ],
            "short": [
                "Fan-1"
            ]
        },
        "Dn": "chassis-1-tray-1-mod-3-fan-1",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentFanModule": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15b576752d3236304d17",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d17"
        },
        "EquipmentFex": null,
        "FanId": 1,
        "FanModuleId": 0,
        "InventoryDeviceInfo": null,
        "ModTime": "2022-10-14T10:35:57.076Z",
        "Model": "UCSX-9508-FAN",
        "ModuleId": 3,
        "Moid": "632b15b576752d3236304d18",
        "ObjectType": "equipment.Fan",
        "OperReason": [],
        "OperState": "OK",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15b576752d3236304d17",
            "ObjectType": "equipment.FanModule",
            "link": "https://www.intersight.com/api/v1/equipment/FanModules/632b15b576752d3236304d17"
        },
        "PartNumber": "73-19422-04 ",
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5ddee0c26972652d33555a3b",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/5ddee0c26972652d33555a3b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "63493b8a6972652d33272ab6",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/63493b8a6972652d33272ab6"
            }
        ],
        "Pid": "UCSX-9508-FAN",
        "Presence": "equipped",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Revision": "0",
        "Rn": "",
        "Serial": "FCH254671AW",
        "SharedScope": "",
        "Sku": "UCSX-9508-FAN",
        "Tags": [],
        "TrayId": 1,
        "Vendor": "Cisco Systems Inc",
        "Vid": "V01"
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment fan'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def is_fan_on(self, item):
        if item is None:
            return False

        if item['Presence'].lower() == 'equipped' and item['OperState'].lower() == 'operable':
            return True

        if item['Presence'].lower() == 'equipped' and item['OperState'].lower() == 'ok':
            return True

        return False

    def get_all(self, max_errors=3, error_timeout=1):
        items = IntersightCommon.get_all(self, max_errors=max_errors, error_timeout=error_timeout)
        if items is not None:
            for item in items:
                item['On'] = self.is_fan_on(item)

        return items

    def get_info(self, moid, cache=True):
        if cache:
            fan_device = self.get_cache_moid(moid)
        else:
            fan_device = self.get(moid)

        if fan_device is None:
            return None

        keys = [
            'Dn',
            'FanId',
            'FanModuleId',
            'Model',
            'ModuleId',
            'OperState',
            'On',
            'PartNumber',
            'Pid',
            'Presence',
            'Serial',
            'Sku',
            'Vendor',
            'TrayId'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            if isinstance(fan_device[key], str):
                info[key] = fan_device[key].strip()
                continue

            info[key] = fan_device[key]

        info['Name'] = 'Fan Module %s - Fan %s' % (
            fan_device['ModuleId'],
            fan_device['FanId']
        )

        if info['Presence'].lower() == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        if info['OperState'].lower() in ['operable', 'ok']:
            info['__Output']['OperState'] = 'Green'
        else:
            info['__Output']['OperState'] = 'Red'

        if info['On']:
            info['__Output']['On'] = 'Green'
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['__Output']['On'] = 'Red'
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        return info
