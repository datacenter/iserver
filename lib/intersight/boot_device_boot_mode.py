from lib.intersight.intersight_common import IntersightCommon


class BootDeviceBootMode(IntersightCommon):
    """Class for intersight bios boot mode objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c016176752d35e44795",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
            }
        ],
        "ClassId": "boot.DeviceBootMode",
        "ComputeBlade": null,
        "ComputeRackUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c016176752d35e44795",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
        },
        "ConfiguredBootMode": "Legacy",
        "CreateTime": "2020-12-20T18:47:09.114Z",
        "DeviceMoId": "5fdf9be76f72612d300a8d81",
        "Dn": "sys/rack-unit-1/boot-precision",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "InventoryDeviceInfo": null,
        "ModTime": "2022-10-25T20:00:14.716Z",
        "Moid": "5fdf9c2d6176752d35e457e2",
        "ObjectType": "boot.DeviceBootMode",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5fdf9be76f72612d300a8d81"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9c016176752d35e44795",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fdf9c016176752d35e44795"
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
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdf9be76f72612d300a8d81",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5fdf9be76f72612d300a8d81"
        },
        "Rn": "",
        "SharedScope": "",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'boot devicebootmode'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}

        info['ConfiguredBootMode'] = item['ConfiguredBootMode']
        info['Moid'] = item['Moid']

        return info
