from lib.intersight.intersight_common import IntersightCommon


class CondAlarm(IntersightCommon):
    """Class for intersight cond alarm objects
    {
        "AccountMoid": "5a58c3ba3768393836cb0f1b",
        "Acknowledge": "None",
        "AcknowledgeBy": "",
        "AcknowledgeTime": "0001-01-01T00:00:00Z",
        "AffectedMo": {
            "ClassId": "mo.MoRef",
            "Moid": "632b15b576752d3236304cd8",
            "ObjectType": "equipment.Psu",
            "link": "https://www.intersight.com/api/v1/equipment/Psus/632b15b576752d3236304cd8"
        },
        "AffectedMoDisplayName": "ucsX/chassis-1/psu-3",
        "AffectedMoId": "",
        "AffectedMoType": "",
        "AffectedObject": "",
        "AncestorMoId": "632b13c876752d32362fc175",
        "AncestorMoType": "equipment.Chassis",
        "Ancestors": [],
        "ClassId": "cond.Alarm",
        "Code": "EquipmentChassisPsuInputLost",
        "CreateTime": "2022-09-21T13:49:14.691Z",
        "CreationTime": "2022-09-21T13:49:14.21Z",
        "Description": "Power supply ucsX/chassis-1/psu-3 has no AC input",
        "DomainGroupMoid": "5b2541957a7662743465d06d",
        "LastTransitionTime": "2022-09-21T13:49:14.21Z",
        "ModTime": "2022-10-14T10:36:06.483Z",
        "Moid": "632b165a65696e2d33b64fac",
        "MsAffectedObject": "",
        "Name": "EquipmentChassisPsuInputLost",
        "ObjectType": "cond.Alarm",
        "OrigSeverity": "Warning",
        "Owners": [
            "5a58c3ba3768393836cb0f1b",
            "632999466f72612d39b26942"
        ],
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
            "Moid": "632999466f72612d39b26942",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/632999466f72612d39b26942"
        },
        "Severity": "Warning",
        "SharedScope": "",
        "Tags": [
            {
                "Key": "cisco.meta.AlarmSource",
                "Value": "Intersight"
            }
        ]
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'cond alarm'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}
        info['__Output'] = {}

        info['AffectedType'] = item['AffectedMo']['ObjectType']
        info['AffectedMoid'] = item['AffectedMo']['Moid']
        info['AffectedName'] = item['AffectedMoDisplayName']
        info['AncestorMoId'] = item['AncestorMoId']
        info['AncestorMoType'] = item['AncestorMoType']
        info['CreateTime'] = item['CreateTime']
        info['Description'] = item['Description']
        info['Moid'] = item['Moid']
        info['Name'] = item['Name']
        info['Code'] = item['Code']

        info['Severity'] = item['Severity']
        if info['Severity'] == 'Critical':
            info['__Output']['Severity'] = 'Red'

        if info['Severity'] == 'Warning':
            info['__Output']['Severity'] = 'Yellow'

        if info['Severity'] == 'Info':
            info['__Output']['Severity'] = 'Blue'

        return info
