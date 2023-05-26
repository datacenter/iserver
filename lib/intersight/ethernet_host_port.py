from lib.intersight.intersight_common import IntersightCommon


class EthernetHostPort(IntersightCommon):
    """Class for intersight ethernet host port objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AcknowledgedPeerInterface": null,
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c976752d32362fc244",
                "ObjectType": "equipment.IoCard",
                "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c976752d32362fc244"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13c876752d32362fc175",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/632b13c876752d32362fc175"
            }
        ],
        "ClassId": "ether.HostPort",
        "CreateTime": "2022-09-21T13:53:33.015Z",
        "DeviceMoId": "632999466f72612d39b26942",
        "Dn": "chassis-1-ioc-1-muxhostport-port-28",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EquipmentIoCardBase": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c976752d32362fc244",
            "ObjectType": "equipment.IoCard",
            "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c976752d32362fc244"
        },
        "MacAddress": "A8:4F:B1:55:4D:9E",
        "ModTime": "2022-11-12T10:34:19.385Z",
        "Mode": "access",
        "ModuleId": 1,
        "Moid": "632b175c6373582d42a0227d",
        "ObjectType": "ether.HostPort",
        "OperSpeed": "auto",
        "OperState": "down",
        "OperStateQual": "admin-down",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "632b13c976752d32362fc244",
            "ObjectType": "equipment.IoCard",
            "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13c976752d32362fc244"
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
        "PortChannelId": 0,
        "PortId": 28,
        "PortType": "Ethernet",
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Rn": "",
        "Role": "unknown",
        "SharedScope": "",
        "SlotId": 1,
        "Speed": "auto",
        "SwitchId": "B",
        "Tags": [],
        "TransceiverType": "unknown"
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'ether hostport'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            host_port = self.get_cache_moid(moid)
        else:
            host_port = self.get(moid)

        if host_port is None:
            return None

        info = {}
        info['Moid'] = host_port['Moid']
        info['Dn'] = host_port['Dn']
        info['Name'] = '%s/%s/%s' % (
            host_port['ModuleId'],
            host_port['SlotId'],
            host_port['PortId']
        )
        info['IoModuleId'] = host_port['EquipmentIoCardBase']['Moid']
        info['MacAddress'] = host_port['MacAddress']
        info['Mode'] = host_port['Mode']
        info['ModuleId'] = host_port['ModuleId']
        info['OperSpeed'] = host_port['OperSpeed']
        info['OperState'] = host_port['OperState']
        info['Up'] = False
        if info['OperState'] == 'up':
            info['Up'] = True
        info['OperStateQual'] = host_port['OperStateQual']
        info['PeerDn'] = host_port['PeerDn']
        info['PeerInterfaceId'] = None
        info['PeerInterfaceType'] = None
        if host_port['PeerInterface'] is not None:
            info['PeerInterfaceId'] = host_port['PeerInterface']['Moid']
            info['PeerInterfaceType'] = host_port['PeerInterface']['ObjectType']
        info['PortChannelId'] = host_port['PortChannelId']
        info['PortId'] = host_port['PortId']
        info['PortType'] = host_port['PortType']
        info['SlotId'] = host_port['SlotId']
        info['Speed'] = host_port['Speed']
        info['SwitchId'] = host_port['SwitchId']
        info['Role'] = host_port['Role']
        info['TransceiverType'] = host_port['TransceiverType']

        return info
