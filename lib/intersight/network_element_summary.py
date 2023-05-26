from lib.intersight.intersight_common import IntersightCommon


class NetworkElementSummary(IntersightCommon):
    """Class for intersight network element summary objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AdminEvacState": "disabled",
        "AdminInbandInterfaceState": "disabled",
        "AlarmSummary": {
            "ClassId": "compute.AlarmSummary",
            "Critical": 0,
            "ObjectType": "compute.AlarmSummary",
            "Warning": 0
        },
        "Ancestors": [],
        "AvailableMemory": "",
        "BundleVersion": "4.2(2c)",
        "Chassis": "",
        "ClassId": "network.ElementSummary",
        "ConfModTs": "",
        "ConfModTsBackup": "",
        "ConnectionStatus": "Connected",
        "CreateTime": "2022-09-20T10:43:23.145Z",
        "DefaultDomain": "",
        "DeviceMoId": "632999466f72612d39b26942",
        "Dn": "switch-FDO26340DE3",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "EthernetMode": "",
        "EthernetSwitchingMode": "end-host",
        "FaultSummary": 0,
        "FcMode": "",
        "FcSwitchingMode": "end-host",
        "Firmware": "",
        "FirmwareVersion": "9.3(5)I42(2c)",
        "InbandIpAddress": "0.0.0.0",
        "InbandIpGateway": "0.0.0.0",
        "InbandIpMask": "255.255.255.0",
        "InbandVlan": 0,
        "Ipv4Address": "",
        "ManagementMode": "Intersight",
        "ModTime": "2022-11-17T08:40:04.045Z",
        "Model": "UCS-FI-6454",
        "Moid": "6329994b76752d3236cd98af",
        "Name": "ucsX FI-A",
        "NumEtherPorts": 54,
        "NumEtherPortsConfigured": 16,
        "NumEtherPortsLinkUp": 16,
        "NumExpansionModules": 0,
        "NumFcPorts": 0,
        "NumFcPortsConfigured": 0,
        "NumFcPortsLinkUp": 0,
        "ObjectType": "network.ElementSummary",
        "OperEvacState": "disabled",
        "Operability": "online",
        "OutOfBandIpAddress": "10.90.90.13",
        "OutOfBandIpGateway": "10.90.90.1",
        "OutOfBandIpMask": "255.255.255.0",
        "OutOfBandIpv4Address": "",
        "OutOfBandIpv4Gateway": "",
        "OutOfBandIpv4Mask": "",
        "OutOfBandIpv6Address": "",
        "OutOfBandIpv6Gateway": "",
        "OutOfBandIpv6Prefix": "",
        "OutOfBandMac": "00:08:31:1B:AA:40",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "PartNumber": "",
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
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Revision": "0",
        "Rn": "",
        "Serial": "FDO26340DE3",
        "SharedScope": "",
        "SourceObjectType": "network.Element",
        "Status": "",
        "SwitchId": "A",
        "SwitchType": "FabricInterconnect",
        "SystemUpTime": "",
        "Tags": [],
        "Thermal": "ok",
        "TotalMemory": 64265,
        "Vendor": "Cisco Systems, Inc.",
        "Version": "9.3(5)I42(2c)"
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'network elementsummary'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}
        info['Moid'] = item['Moid']
        info['Name'] = item['Name']
        if item['AlarmSummary']['Warning'] == 0 and item['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Healthy'
            info['HealthSummary'] = 'Healthy'
        if item['AlarmSummary']['Warning'] > 0 and item['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Warnings'
            info['HealthSummary'] = 'Warnings (%s)' % (item['AlarmSummary']['Warning'])
        if item['AlarmSummary']['Critical'] > 0:
            info['Health'] = 'Critical'
            info['HealthSummary'] = 'Critical (%s)' % (item['AlarmSummary']['Critical'])

        info['ConnectionStatus'] = item['ConnectionStatus']
        info['Dn'] = item['Dn']
        info['Model'] = item['Model']
        info['NumEtherPorts'] = item['NumEtherPorts']
        info['NumEtherPortsConfigured'] = item['NumEtherPortsConfigured']
        info['NumEtherPortsLinkUp'] = item['NumEtherPortsLinkUp']
        info['NumEtherPortsSummary'] = '%s/%s/%s' % (
            info['NumEtherPortsLinkUp'],
            info['NumEtherPortsConfigured'],
            info['NumEtherPorts']
        )
        info['OutOfBandIpAddress'] = item['OutOfBandIpAddress']
        info['OutOfBandIpGateway'] = item['OutOfBandIpGateway']
        info['OutOfBandIpMask'] = item['OutOfBandIpMask']
        info['Serial'] = item['Serial']
        info['SwitchId'] = item['SwitchId']
        info['Version'] = item['Version']

        return info
