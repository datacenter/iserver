from lib.intersight.intersight_common import IntersightCommon


class RunningFirmware(IntersightCommon):
    """Class for intersight running firmware objects

    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4f076176752d32d54b2a",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/5e8c4f076176752d32d54b2a"
        },
        {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed26176752d32d51c40",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5e8c4ed26176752d32d51c40"
        }
        ],
        "BiosUnit": null,
        "ClassId": "firmware.RunningFirmware",
        "Component": "system",
        "CreateTime": "2020-04-07T09:59:29.217Z",
        "DeviceMoId": "5e8c4ecd6f72612d302b11a6",
        "Dn": "sys/rack-unit-1/mgmt/fw-system",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "GraphicsCard": null,
        "InventoryDeviceInfo": null,
        "ManagementController": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4f076176752d32d54b2a",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/5e8c4f076176752d32d54b2a"
        },
        "ModTime": "2022-05-09T13:36:01.248Z",
        "Moid": "5e8c4f016176752d32d5448c",
        "NetworkElements": [],
        "ObjectType": "firmware.RunningFirmware",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5e8c4ecd6f72612d302b11a6"
        ],
        "PackageVersion": "",
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4f076176752d32d54b2a",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/5e8c4f076176752d32d54b2a"
        },
        "PciSwitch": null,
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
            "Moid": "5e8c4ecd6f72612d302b11a6",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5e8c4ecd6f72612d302b11a6"
        },
        "Rn": "",
        "SharedScope": "",
        "StorageController": null,
        "StorageFlexFlashController": null,
        "StoragePhysicalDisk": null,
        "Tags": [],
        "Type": "blade-controller",
        "Version": "4.1(2f)"
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'firmware runningfirmware'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_firmware_name(self, info):
        if info['Type'] == 'adaptor':
            return 'Adapter'

        if info['Type'] == 'blade-bios':
            return 'BIOS'

        if info['Type'] == 'local-disk':
            return 'Disk'

        if info['Type'] == 'storage-controller':
            return 'Storage Controller'

        if info['Component'] == 'boot-loader' and info['Type'] == 'blade-controller':
            return 'Board Controller'

        if info['Component'] == 'system' and info['Type'] == 'blade-controller':
            return 'CIMC Controller'

        return ''

    def get_info(self, managed_object):
        keys = [
            'Component',
            'Dn',
            'Type',
            'PackageVersion',
            'Version'
        ]
        info = {}
        for key in keys:
            info[key] = managed_object[key].replace('\n', '')

        info['Name'] = self.get_firmware_name(info)

        return info

    def get_firmware_version(self, managed_objects):
        for managed_object in managed_objects:
            if managed_object['Component'] == 'system' and managed_object['Type'] == 'blade-controller':
                return managed_object['Version']
        return None
