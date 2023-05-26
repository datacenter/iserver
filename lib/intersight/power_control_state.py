from lib.intersight.intersight_common import IntersightCommon


class PowerControlState(IntersightCommon):
    """Class for intersight power control state objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AllocatedPower": 0,
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "632b13ca76752d32362fc2b9",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13ca76752d32362fc2b9"
            }
        ],
        "ClassId": "power.ControlState",
        "CreateTime": "2022-09-22T13:58:12.808Z",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13ca76752d32362fc2b9",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13ca76752d32362fc2b9"
        },
        "ExtendedPowerCapacity": "Enabled",
        "GridMaxPower": 7000,
        "MaxRequiredPower": 8079,
        "MinRequiredPower": 4190,
        "ModTime": "2022-11-03T02:42:48.686Z",
        "Moid": "632c69f476752d32369419ce",
        "N1MaxPower": 10500,
        "N2MaxPower": 7000,
        "NonRedundantMaxPower": 12174,
        "ObjectType": "power.ControlState",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13ca76752d32362fc2b9",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13ca76752d32362fc2b9"
        },
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
        "PowerRebalancing": "Enabled",
        "PowerSaveMode": "Enabled",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "SharedScope": "",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'power controlstate'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        keys = [
            'Moid',
            'AllocatedPower',
            'ExtendedPowerCapacity',
            'GridMaxPower',
            'MaxRequiredPower',
            'MinRequiredPower',
            'N1MaxPower',
            'N2MaxPower',
            'NonRedundantMaxPower',
            'PowerRebalancing',
            'PowerSaveMode'
        ]

        info = {}
        for key in keys:
            info[key] = item[key]

        if item['AllocatedPower'] == 0:
            item['AllocatedBudget'] = 'Not set'
        else:
            item['AllocatedBudget'] = item['AllocatedPower']

        keys = [
            'Moid',
            'AllocatedPower',
            'GridMaxPower',
            'MaxRequiredPower',
            'MinRequiredPower',
            'N1MaxPower',
            'N2MaxPower',
            'NonRedundantMaxPower'
        ]

        for key in keys:
            info['%sUnit' % (key)] = '%s W' % (str(info[key]))

        return info
