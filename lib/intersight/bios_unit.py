from lib.intersight.intersight_common import IntersightCommon


class BiosUnit(IntersightCommon):
    """Class for intersight bios unit objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
            }
        ],
        "ClassId": "bios.Unit",
        "ComputeBlade": null,
        "ComputeRackUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
        },
        "CreateTime": "2022-09-02T07:09:58.416Z",
        "DeviceMoId": "61c35fa36f72612d3005590c",
        "Dn": "sys/rack-unit-3/bios",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "InitSeq": "0xb1:0xad:0xb2:0x92:0xa2:0xa2:0xa2:0xa2:0xa2:0xa2:0xa0:0x99:0xa2:0xa2:0xa2:0xa2:0xa0:0x92:0xb4:0xb4",
        "InitTs": "2022-09-02T07:33:38.461",
        "InventoryDeviceInfo": null,
        "ModTime": "2022-09-02T07:33:38.549Z",
        "Model": "UCSC-C220-M4S",
        "Moid": "6311ac4676752d31398e5336",
        "ObjectType": "bios.Unit",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "61c35fa36f72612d3005590c"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6311aae876752d31398e1a50",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/6311aae876752d31398e1a50"
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
        "Presence": "",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "61c35fa36f72612d3005590c",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/61c35fa36f72612d3005590c"
        },
        "Revision": "0",
        "Rn": "",
        "RunningFirmware": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "6311ac4676752d31398e5338",
            "ObjectType": "firmware.RunningFirmware",
            "link": "https://www.intersight.com/api/v1/firmware/RunningFirmwares/6311ac4676752d31398e5338"
            }
        ],
        "Serial": "",
        "SharedScope": "",
        "SystemBootOrder": null,
        "Tags": [],
        "Vendor": "Cisco Systems, Inc."
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'bios unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_running_firmware_id(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        for running_firmware in item['RunningFirmware']:
            if running_firmware['ObjectType'] == 'firmware.RunningFirmware':
                return running_firmware['Moid']

        return None
