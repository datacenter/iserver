from lib.intersight.intersight_common import IntersightCommon


class AdapterHostEthInterface(IntersightCommon):
    """Class for intersight adapter host ethernet interface objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "AcknowledgedPeerInterface": null,
        "AdapterUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c50046176752d32d64486",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d64486"
        },
        "AdminState": "",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5e8c50046176752d32d64486",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d64486"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "5e8c4ed26176752d32d51c40",
                "ObjectType": "compute.RackUnit",
                "link": "https://www.intersight.com/api/v1/compute/RackUnits/5e8c4ed26176752d32d51c40"
            }
        ],
        "ClassId": "adapter.HostEthInterface",
        "CreateTime": "2020-04-07T10:03:45.983Z",
        "DeviceMoId": "5e8c4ecd6f72612d302b11a6",
        "Dn": "sys/rack-unit-1/network-adapter-1/eth-3",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EpDn": "",
        "HostEthInterfaceId": 3,
        "InterfaceType": "",
        "InventoryDeviceInfo": null,
        "MacAddress": "3c:fd:fe:cb:eb:02",
        "ModTime": "2022-05-09T13:36:01.032Z",
        "Moid": "5e8c50016176752d32d64236",
        "Name": "eth-3",
        "ObjectType": "adapter.HostEthInterface",
        "OperReason": [],
        "OperState": "",
        "Operability": "",
        "OriginalMacAddress": "",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5e8c4ecd6f72612d302b11a6"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c50046176752d32d64486",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/5e8c50046176752d32d64486"
        },
        "PciAddr": "",
        "PeerDn": "",
        "PeerInterface": null,
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
        "PinGroupName": "",
        "PinnedInterface": null,
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ecd6f72612d302b11a6",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/5e8c4ecd6f72612d302b11a6"
        },
        "Rn": "",
        "SharedScope": "",
        "Tags": [],
        "VirtualizationPreference": "",
        "VnicDn": ""
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter hostethinterface'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            adapter_interface = self.get_cache_moid(moid)
        else:
            adapter_interface = self.get(moid)

        if adapter_interface is None:
            return None

        info = {}
        info['Moid'] = adapter_interface['Moid']
        info['Type'] = 'HostEth'
        info['Dn'] = adapter_interface['Dn']
        info['AdapterUnitId'] = adapter_interface['AdapterUnit']['Moid']
        info['AdminState'] = adapter_interface['AdminState']
        info['HostEthInterfaceId'] = adapter_interface['HostEthInterfaceId']
        info['InterfaceType'] = adapter_interface['InterfaceType']
        info['MacAddress'] = adapter_interface['MacAddress']
        info['Name'] = adapter_interface['Name']
        info['OperState'] = adapter_interface['OperState']
        info['Operability'] = adapter_interface['Operability']
        info['PciAddr'] = adapter_interface['PciAddr']
        info['PeerDn'] = adapter_interface['PeerDn']
        info['PeerInterface'] = adapter_interface['PeerInterface']

        return info
