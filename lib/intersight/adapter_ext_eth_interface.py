from lib.intersight.intersight_common import IntersightCommon


class AdapterExtEthInterface(IntersightCommon):
    """Class for intersight adapter external ethernet interface objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AcknowledgedPeerInterface": {
            "ClassId": "mo.MoRef",
            "Moid": "632b158c6373582d415a5ac2",
            "ObjectType": "ether.HostPort",
            "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac2"
        },
        "AdapterUnit": {
            "ClassId": "mo.MoRef",
            "Moid": "632b188376752d3236311708",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/632b188376752d3236311708"
        },
        "AdminState": "Enabled",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b188376752d3236311708",
                "ObjectType": "adapter.Unit",
                "link": "https://www.intersight.com/api/v1/adapter/Units/632b188376752d3236311708"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b163d76752d323630734f",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b163d76752d323630734f"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "ClassId": "adapter.ExtEthInterface",
        "CreateTime": "2022-09-21T13:58:35.052Z",
        "DeviceMoId": "632b16036f72612d39c67825",
        "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-1",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EpDn": "",
        "ExtEthInterfaceId": "1",
        "InterfaceType": "",
        "InventoryDeviceInfo": null,
        "MacAddress": "48:2E:72:E4:50:29",
        "ModTime": "2022-11-07T18:32:32.651Z",
        "Moid": "632b188b76752d3236311bb7",
        "ObjectType": "adapter.ExtEthInterface",
        "OperState": "",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942",
            "632b16036f72612d39c67825"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b188376752d3236311708",
            "ObjectType": "adapter.Unit",
            "link": "https://www.intersight.com/api/v1/adapter/Units/632b188376752d3236311708"
        },
        "PeerAggrPortId": 0,
        "PeerDn": "chassis-1-ioc-2-muxhostport-port-5",
        "PeerInterface": {
            "ClassId": "mo.MoRef",
            "Moid": "632b158c6373582d415a5ac2",
            "ObjectType": "ether.HostPort",
            "link": "https://www.intersight.com/api/v1/ether/HostPorts/632b158c6373582d415a5ac2"
        },
        "PeerPortId": 5,
        "PeerSlotId": 1,
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
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632b16036f72612d39c67825",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632b16036f72612d39c67825"
        },
        "Rn": "",
        "SharedScope": "",
        "SwitchId": "A",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'adapter extethinterface'
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
        info['Dn'] = adapter_interface['Dn']
        info['AdapterUnitId'] = adapter_interface['AdapterUnit']['Moid']
        info['AdminState'] = adapter_interface['AdminState']
        info['InterfaceId'] = adapter_interface['ExtEthInterfaceId']
        info['MacAddress'] = adapter_interface['MacAddress'].lower()
        info['SwitchId'] = adapter_interface['SwitchId']

        info['PeerHostPortId'] = None
        if adapter_interface['AcknowledgedPeerInterface'] is not None:
            if adapter_interface['AcknowledgedPeerInterface']['ObjectType'] == 'ether.HostPort':
                info['PeerHostPortId'] = adapter_interface['AcknowledgedPeerInterface']['Moid']
        info['PeerAggrPortId'] = adapter_interface['PeerAggrPortId']
        info['PeerDn'] = adapter_interface['PeerDn']
        info['PeerPortId'] = adapter_interface['PeerPortId']
        info['PeerSlotId'] = adapter_interface['PeerSlotId']

        return info
