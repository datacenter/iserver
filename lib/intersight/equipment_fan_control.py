from lib.intersight.intersight_common import IntersightCommon


class EquipmentFanControl(IntersightCommon):
    """Class for intersight equipment fan control objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "632b13ca76752d32362fc2b9",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13ca76752d32362fc2b9"
            }
        ],
        "ClassId": "equipment.FanControl",
        "CreateTime": "2022-09-21T13:46:28.525Z",
        "DeviceMoId": "",
        "Dn": "chassis-2-fan-control",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13ca76752d32362fc2b9",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13ca76752d32362fc2b9"
        },
        "InventoryDeviceInfo": null,
        "ModTime": "2022-10-14T10:35:58.425Z",
        "Mode": "LowPower",
        "Model": "",
        "Moid": "632b15b476752d3236304be5",
        "ObjectType": "equipment.FanControl",
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
        "Presence": "",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "",
        "SharedScope": "",
        "Tags": [],
        "Vendor": ""
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment fancontrol'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_info(self, moid):
        item = self.get(moid)
        if item is None:
            return None

        keys = [
            'Moid',
            'Dn',
            'Mode'
        ]

        info = {}
        for key in keys:
            info[key] = item[key]

        return info
