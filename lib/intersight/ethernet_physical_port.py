from lib.intersight.intersight_common import IntersightCommon


class EthernetPhysicalPort(IntersightCommon):
    """Class for intersight ethernet physical port objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AcknowledgedPeerInterface": null,
        "AdminSpeed": "",
        "AdminState": "Enabled",
        "AggregatePortId": 0,
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6329994b76752d3236cd98b3",
                "ObjectType": "port.Group",
                "link": "https://www.intersight.com/api/v1/port/Groups/6329994b76752d3236cd98b3"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6329994b76752d3236cd98b1",
                "ObjectType": "equipment.SwitchCard",
                "link": "https://www.intersight.com/api/v1/equipment/SwitchCards/6329994b76752d3236cd98b1"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6329994b76752d3236cd98af",
                "ObjectType": "network.Element",
                "link": "https://www.intersight.com/api/v1/network/Elements/6329994b76752d3236cd98af"
            }
        ],
        "ClassId": "ether.PhysicalPort",
        "CreateTime": "2022-09-20T10:43:23.203Z",
        "DeviceMoId": "632999466f72612d39b26942",
        "DisplayNames": {
            "hierarchical": [
            "ethport-21"
            ],
            "short": [
            "Ethport-21"
            ]
        },
        "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-21",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "InventoryDeviceInfo": null,
        "LicenseGrace": "",
        "LicenseState": "",
        "MacAddress": "00:08:31:1B:AA:5C",
        "ModTime": "2022-11-12T18:32:04.303Z",
        "Mode": "fex-fabric",
        "Moid": "6329994b76752d3236cd98dd",
        "Name": "",
        "ObjectType": "ether.PhysicalPort",
        "OperSpeed": "25G",
        "OperState": "up",
        "OperStateQual": "none",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "6329994b76752d3236cd98b3",
            "ObjectType": "port.Group",
            "link": "https://www.intersight.com/api/v1/port/Groups/6329994b76752d3236cd98b3"
        },
        "PeerDn": "",
        "PeerInterface": null,
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
        "PortChannelId": 1025,
        "PortGroup": {
            "ClassId": "mo.MoRef",
            "Moid": "6329994b76752d3236cd98b3",
            "ObjectType": "port.Group",
            "link": "https://www.intersight.com/api/v1/port/Groups/6329994b76752d3236cd98b3"
        },
        "PortId": 21,
        "PortSubGroup": null,
        "PortType": "",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Rn": "",
        "Role": "Server",
        "SharedScope": "",
        "SlotId": 1,
        "SwitchId": "A",
        "Tags": [],
        "TransceiverType": "SFP-25G-AOC2M"
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether physicalport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['Name'] = '%s/%s' % (
            managed_object['SlotId'],
            managed_object['PortId']
        )
        info['AdminState'] = managed_object['AdminState']
        info['AggregatePortId'] = managed_object['AggregatePortId']
        info['MacAddress'] = managed_object['MacAddress']
        info['Mode'] = managed_object['Mode']
        info['OperSpeed'] = managed_object['OperSpeed']
        info['OperState'] = managed_object['OperState']
        info['PortId'] = managed_object['PortId']
        info['PortChannelId'] = managed_object['PortChannelId']
        info['Role'] = managed_object['Role']
        info['SlotId'] = managed_object['SlotId']
        info['SwitchId'] = managed_object['SwitchId']
        info['TransceiverType'] = managed_object['TransceiverType']

        return info
