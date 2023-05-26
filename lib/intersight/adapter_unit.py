from lib.intersight.intersight_common import IntersightCommon


class AdapterUnit(IntersightCommon):
    """Class for intersight adapter unit objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AdapterId": "UCSX-V4-Q25GML_FCH26217FVU",
        "AdapterUnitExpander": null,
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b174e76752d323630bb47",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b174e76752d323630bb47"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "BaseMacAddress": "48:2E:72:E4:50:40",
        "ClassId": "adapter.Unit",
        "ComputeBlade": {
            "ClassId": "mo.MoRef",
            "Moid": "632b174e76752d323630bb47",
            "ObjectType": "compute.Blade",
            "link": "https://www.intersight.com/api/v1/compute/Blades/632b174e76752d323630bb47"
        },
        "ComputeRackUnit": null,
        "ConnectionStatus": "",
        "Controller": {
            "ClassId": "mo.MoRef",
            "Moid": "632b19a876752d3236316cb7",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/632b19a876752d3236316cb7"
        },
        "CreateTime": "2022-09-21T14:03:20.004Z",
        "DeviceMoId": "632b165e6f72612d39c67cd5",
        "DisplayNames": {
            "hierarchical": [
            "adapter-UCSX-V4-Q25GML_FCH26217FVU"
            ],
            "short": [
            "Adapter-UCSX-V4-Q25GML_FCH26217FVU"
            ]
        },
        "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "ExtEthIfs": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b19af76752d3236316ea9",
                "ObjectType": "adapter.ExtEthInterface",
                "link": "https://www.intersight.com/api/v1/adapter/ExtEthInterfaces/632b19af76752d3236316ea9"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b19af76752d3236316eaa",
                "ObjectType": "adapter.ExtEthInterface",
                "link": "https://www.intersight.com/api/v1/adapter/ExtEthInterfaces/632b19af76752d3236316eaa"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b19af76752d3236316eab",
                "ObjectType": "adapter.ExtEthInterface",
                "link": "https://www.intersight.com/api/v1/adapter/ExtEthInterfaces/632b19af76752d3236316eab"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b19af76752d3236316eac",
                "ObjectType": "adapter.ExtEthInterface",
                "link": "https://www.intersight.com/api/v1/adapter/ExtEthInterfaces/632b19af76752d3236316eac"
            }
        ],
        "HostEthIfs": [],
        "HostFcIfs": [],
        "HostIscsiIfs": [],
        "Integrated": "",
        "InventoryDeviceInfo": null,
        "ModTime": "2022-10-14T10:35:56.755Z",
        "Model": "UCSX-V4-Q25GML",
        "Moid": "632b19a776752d3236316cb1",
        "ObjectType": "adapter.Unit",
        "OperState": "OK",
        "Operability": "",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942",
            "632b165e6f72612d39c67cd5"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b174e76752d323630bb47",
            "ObjectType": "compute.Blade",
            "link": "https://www.intersight.com/api/v1/compute/Blades/632b174e76752d323630bb47"
        },
        "PartNumber": "73-20185-03",
        "PciSlot": "SlotID:0-MLOM",
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
        "Power": "",
        "Presence": "equipped",
        "PreviousFru": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632b165e6f72612d39c67cd5",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632b165e6f72612d39c67cd5"
        },
        "Revision": "",
        "Rn": "",
        "Serial": "FCH26217FVU",
        "SharedScope": "",
        "Tags": [],
        "Thermal": "",
        "Vendor": "Cisco Systems Inc",
        "Vid": ""
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter unit'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            adapter_unit = self.get_cache_moid(moid)
        else:
            adapter_unit = self.get(moid)

        if adapter_unit is None:
            return None

        info = {}
        info['Moid'] = adapter_unit['Moid']
        info['Dn'] = adapter_unit['Dn']
        info['AdapterId'] = adapter_unit['AdapterId']
        info['Name'] = 'Adapter %s' % (info['AdapterId'])
        info['BaseMacAddress'] = adapter_unit['BaseMacAddress']
        if adapter_unit['ComputeBlade'] is not None:
            info['ComputeNodeMoid'] = adapter_unit['ComputeBlade']['Moid']
        if adapter_unit['ComputeRackUnit'] is not None:
            info['ComputeNodeMoid'] = adapter_unit['ComputeRackUnit']['Moid']

        info['ExtEthIfsIds'] = []
        for interface in adapter_unit['ExtEthIfs']:
            info['ExtEthIfsIds'].append(interface['Moid'])
        info['ExtEthIfsCount'] = len(info['ExtEthIfsIds'])

        info['HostEthIfsIds'] = []
        for interface in adapter_unit['HostEthIfs']:
            info['HostEthIfsIds'].append(interface['Moid'])
        info['HostEthIfsCount'] = len(info['HostEthIfsIds'])

        info['HostFcIfsIds'] = []
        for interface in adapter_unit['HostFcIfs']:
            info['HostFcIfsIds'].append(interface['Moid'])
        info['HostFcIfsCount'] = len(info['HostFcIfsIds'])

        info['HostIscsiIfsIds'] = []
        for interface in adapter_unit['HostIscsiIfs']:
            info['HostIscsiIfsIds'].append(interface['Moid'])
        info['HostIscsiIfsCount'] = len(info['HostIscsiIfsIds'])

        info['Model'] = adapter_unit['Model']
        info['OperState'] = adapter_unit['OperState']
        info['PartNumber'] = adapter_unit['PartNumber']
        info['Presence'] = adapter_unit['Presence']
        info['Healthy'] = False
        if info['Presence'] == 'equipped' and info['OperState'] == 'OK':
            info['Healthy'] = True
        info['PciSlot'] = adapter_unit['PciSlot']
        info['Thermal'] = adapter_unit['Thermal']
        info['Serial'] = adapter_unit['Serial']
        info['Vendor'] = adapter_unit['Vendor']

        return info
