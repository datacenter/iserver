from lib.intersight.intersight_common import IntersightCommon


class EquipmentChassis(IntersightCommon):
    """Class for intersight equipment chassis objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "AlarmSummary": {
            "ClassId": "compute.AlarmSummary",
            "Critical": 0,
            "ObjectType": "compute.AlarmSummary",
            "Warning": 2
        },
        "Ancestors": [],
        "Blades": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b976752d3236304e93",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b15b976752d3236304e93"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b976752d3236304ea8",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b15b976752d3236304ea8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b163a76752d3236307256",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b163a76752d3236307256"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b163b76752d32363072e7",
                "ObjectType": "compute.Blade",
                "link": "https://www.intersight.com/api/v1/compute/Blades/632b163b76752d32363072e7"
            }
        ],
        "ChassisId": 2,
        "ClassId": "equipment.Chassis",
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "CreateTime": "2022-09-21T13:38:18.807Z",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "DeviceMoId": "632999466f72612d39b26942",
        "Dn": "chassis-2",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "ExpanderModules": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b476752d3236304bd4",
                "ObjectType": "equipment.ExpanderModule",
                "link": "https://www.intersight.com/api/v1/equipment/ExpanderModules/632b15b476752d3236304bd4"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b15b476752d3236304be1",
                "ObjectType": "equipment.ExpanderModule",
                "link": "https://www.intersight.com/api/v1/equipment/ExpanderModules/632b15b476752d3236304be1"
            }
        ],
        "FanControl": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15b476752d3236304be5",
            "ObjectType": "equipment.FanControl",
            "link": "https://www.intersight.com/api/v1/equipment/FanControls/632b15b476752d3236304be5"
        },
        "Fanmodules": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f576752d3236941a5b",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632c69f576752d3236941a5b"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f576752d3236941a70",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632c69f576752d3236941a70"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f576752d3236941aa4",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632c69f576752d3236941aa4"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f576752d3236941ab3",
                "ObjectType": "equipment.FanModule",
                "link": "https://www.intersight.com/api/v1/equipment/FanModules/632c69f576752d3236941ab3"
            }
        ],
        "FaultSummary": 0,
        "InventoryDeviceInfo": null,
        "Ioms": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632b13ca76752d32362fc2c0",
                "ObjectType": "equipment.IoCard",
                "link": "https://www.intersight.com/api/v1/equipment/IoCards/632b13ca76752d32362fc2c0"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c68b376752d323693c512",
                "ObjectType": "equipment.IoCard",
                "link": "https://www.intersight.com/api/v1/equipment/IoCards/632c68b376752d323693c512"
            }
        ],
        "LocatorLed": null,
        "ManagementInterface": null,
        "ManagementMode": "Intersight",
        "ModTime": "2022-10-14T10:35:57.395Z",
        "Model": "UCSX-9508",
        "Moid": "632b13ca76752d32362fc2b9",
        "Name": "ucsX-2",
        "ObjectType": "equipment.Chassis",
        "OperReason": [],
        "OperState": "OK",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
        "PartNumber": "68-6847-03  ",
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
        "Pid": "UCSX-9508",
        "PlatformType": "",
        "PowerControlState": {
            "ClassId": "mo.MoRef",
            "Moid": "632c69f476752d32369419ce",
            "ObjectType": "power.ControlState",
            "link": "https://www.intersight.com/api/v1/power/ControlStates/632c69f476752d32369419ce"
        },
        "Presence": "",
        "PreviousFru": null,
        "ProductName": "Cisco UCSX 9508 Chassis",
        "PsuControl": {
            "ClassId": "mo.MoRef",
            "Moid": "632c69f476752d32369419c8",
            "ObjectType": "equipment.PsuControl",
            "link": "https://www.intersight.com/api/v1/equipment/PsuControls/632c69f476752d32369419c8"
        },
        "Psus": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419a8",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419a8"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419ac",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419ac"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419b0",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419b0"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419b4",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419b4"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419ba",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419ba"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "632c69f476752d32369419c1",
                "ObjectType": "equipment.Psu",
                "link": "https://www.intersight.com/api/v1/equipment/Psus/632c69f476752d32369419c1"
            }
        ],
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Revision": "0",
        "Rn": "",
        "Sasexpanders": [],
        "Serial": "FOX2615P18G",
        "SharedScope": "",
        "Siocs": [],
        "Sku": "UCSX-9508",
        "StorageEnclosures": [],
        "Tags": [],
        "Vendor": "Cisco Systems Inc",
        "Vid": "V01",
        "VirtualDriveContainer": []
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'equipment chassis'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def filter(self, name_filter='', serial_filter='', model_filter=''):
        items = IntersightCommon.get_all(self)
        if items is None:
            return None

        if len(name_filter) == 0 and len(serial_filter) == 0 and len(model_filter) == 0:
            return items

        filtered = []
        for item in items:
            if len(name_filter) > 0 and name_filter.lower() not in item['Name'].lower():
                continue

            if len(serial_filter) > 0 and serial_filter.lower() not in item['Serial'].lower():
                continue

            if len(model_filter) > 0 and model_filter.lower() not in item['Model'].lower():
                continue

            filtered.append(item)

        return filtered

    def get_summary(self, chassis):
        info = {}
        info['__Output'] = {}

        info['Moid'] = chassis['Moid']
        info['Dn'] = chassis['Dn']
        info['Blades'] = len(chassis['Blades'])
        info['Name'] = chassis['Name']
        info['Model'] = chassis['Model']
        info['Serial'] = chassis['Serial']

        if chassis['AlarmSummary']['Warning'] == 0 and chassis['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Healthy'
            info['HealthSummary'] = 'Healthy'
            info['__Output']['Health'] = 'Green'
        if chassis['AlarmSummary']['Warning'] > 0 and chassis['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Warnings'
            info['HealthSummary'] = 'Warnings (%s)' % (chassis['AlarmSummary']['Warning'])
            info['__Output']['Health'] = 'Yellow'
        if chassis['AlarmSummary']['Critical'] > 0:
            info['Health'] = 'Critical'
            info['HealthSummary'] = 'Critical (%s)' % (chassis['AlarmSummary']['Critical'])
            info['__Output']['Health'] = 'Red'

        info['UcsDomain'] = ''
        if 'DeviceHostname' in chassis['RegisteredDevice']:
            info['UcsDomain'] = chassis['RegisteredDevice']['DeviceHostname'][0]

        return info
