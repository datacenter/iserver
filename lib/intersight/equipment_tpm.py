from lib.intersight.intersight_common import IntersightCommon


class EquipmentTpm(IntersightCommon):
    """Class for intersight equipment tpm objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "ActivationStatus": "unknown",
        "AdminState": "unknown",
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
        "ClassId": "equipment.Tpm",
        "ComputeBoard": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed96176752d32d52214",
            "ObjectType": "compute.Board",
            "link": "https://www.intersight.com/api/v1/compute/Boards/5e8c4ed96176752d32d52214"
        },
        "CreateTime": "2020-04-07T10:02:13.533Z",
        "DeviceMoId": "5e8c4ecd6f72612d302b11a6",
        "Dn": "sys/rack-unit-1/board/tpm",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "FirmwareVersion": "",
        "InventoryDeviceInfo": null,
        "ModTime": "2022-05-09T13:36:01.073Z",
        "Model": "NA",
        "Moid": "5e8c4fa56176752d32d5e4bd",
        "ObjectType": "equipment.Tpm",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5e8c4ecd6f72612d302b11a6"
        ],
        "Ownership": "unknown",
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
        "Presence": "empty",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ecd6f72612d302b11a6",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5e8c4ecd6f72612d302b11a6"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "NA",
        "SharedScope": "",
        "Tags": [],
        "TpmId": 0,
        "Vendor": "NA",
        "Version": "NA"
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment tpm'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'ActivationStatus',
            'AdminState',
            'FirmwareVersion',
            'Model',
            'Moid',
            'Presence',
            'Serial',
            'TpmId',
            'Vendor',
            'Version'
        ]

        for key in keys:
            info[key] = item[key]

        if info['ActivationStatus'].lower() == 'activated':
            info['__Output']['ActivationStatus'] = 'Green'

        if info['ActivationStatus'].lower() == 'unknown':
            info['__Output']['ActivationStatus'] = 'Yellow'

        if info['AdminState'].lower() == 'unknown':
            info['__Output']['AdminState'] = 'Yellow'

        if info['AdminState'].lower() == 'enabled':
            info['__Output']['AdminState'] = 'Green'

        if info['AdminState'].lower() == 'disabled':
            info['__Output']['AdminState'] = 'Red'

        if info['Presence'].lower() == 'empty':
            info['__Output']['Presence'] = 'Yellow'
        else:
            info['__Output']['Presence'] = 'Green'

        return info
