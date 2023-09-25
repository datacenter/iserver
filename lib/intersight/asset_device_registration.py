from lib.intersight.intersight_common import IntersightCommon


class AssetDeviceRegistration(IntersightCommon):
    """Class for intersight asset device registration objects
    {
    "Account": {
        "ClassId": "mo.MoRef",
        "Moid": "5a58c3ba3768393836cb0f1b",
        "ObjectType": "iam.Account",
        "link": "https://www.intersight.com/api/v1/iam/Accounts/5a58c3ba3768393836cb0f1b"
    },
    "AccountMoid": "5a58c3ba3768393836cb0f1b",
    "Ancestors": [],
    "ApiVersion": 11,
    "AppPartitionNumber": 125,
    "ClaimedByUser": {
        "ClassId": "mo.MoRef",
        "Moid": "5a58c41a3768393836cb10bc",
        "ObjectType": "iam.User",
        "link": "https://www.intersight.com/api/v1/iam/Users/5a58c41a3768393836cb10bc"
    },
    "ClaimedByUserName": "sesousa@cisco.com",
    "ClaimedTime": "2022-09-20T10:43:18.327Z",
    "ClassId": "asset.DeviceRegistration",
    "ClusterMembers": [
        {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26945",
        "ObjectType": "asset.ClusterMember",
        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/632999466f72612d39b26945"
        },
        {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26946",
        "ObjectType": "asset.ClusterMember",
        "link": "https://www.intersight.com/api/v1/asset/ClusterMembers/632999466f72612d39b26946"
        }
    ],
    "ConnectionId": "e53fb7c94631f12a96832ed63dcdb8d4:8e008439-dc1d-4f25-89b9-8471e6262801",
    "ConnectionReason": "",
    "ConnectionStatus": "Connected",
    "ConnectionStatusLastChangeTime": "2022-11-13T03:27:22.596Z",
    "ConnectorVersion": "1.0.11-2396",
    "CreateTime": "2022-09-20T10:43:18.301Z",
    "DeviceClaim": {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26939",
        "ObjectType": "asset.DeviceClaim",
        "link": "https://www.intersight.com/api/v1/asset/DeviceClaims/632999466f72612d39b26939"
    },
    "DeviceConfiguration": {
        "ClassId": "mo.MoRef",
        "Moid": "632999466f72612d39b26943",
        "ObjectType": "asset.DeviceConfiguration",
        "link": "https://www.intersight.com/api/v1/asset/DeviceConfigurations/632999466f72612d39b26943"
    },
    "DeviceExternalIpAddress": "62.28.62.162",
    "DeviceHostname": [
        "ucsX"
    ],
    "DeviceIpAddress": [
        "10.90.90.13",
        "10.90.90.14"
    ],
    "DisplayNames": {
        "hierarchical": [
        "[ucsX]"
        ],
        "short": [
        "[ucsX]"
        ]
    },
    "DomainGroup": {
        "ClassId": "mo.MoRef",
        "Moid": "5b2541957a7662743465d06d",
        "ObjectType": "iam.DomainGroup",
        "link": "https://www.intersight.com/api/v1/iam/DomainGroups/5b2541957a7662743465d06d"
    },
    "DomainGroupMoid": "5b2541957a7662743465d06d",
    "ExecutionMode": "Normal",
    "ModTime": "2022-11-13T03:27:22.648Z",
    "Moid": "632999466f72612d39b26942",
    "ObjectType": "asset.DeviceRegistration",
    "Owners": [
        "5a58c3ba3768393836cb0f1b",
        "632999466f72612d39b26942"
    ],
    "ParentConnection": null,
    "ParentSignature": null,
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
    "Pid": [
        "UCS-FI-6454"
    ],
    "PlatformType": "UCSFIISM",
    "ProxyApp": "astro",
    "PublicAccessKey": "",
    "ReadOnly": false,
    "SecurityToken": null,
    "Serial": [
        "FDO26340DE3",
        "FDO26340CVC"
    ],
    "SharedScope": "",
    "Tags": [
        {
        "Key": "cisco.meta.ManagementMode",
        "Value": "Intersight"
        }
    ],
    "Vendor": "Cisco Systems, Inc."
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'asset deviceregistration'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        info['Moid'] = managed_object['Moid']
        info['ClaimedByUserName'] = managed_object['ClaimedByUserName']
        info['ClaimedTime'] = managed_object['ClaimedTime']
        info['PlatformType'] = managed_object['PlatformType']
        info['ConnectorVersion'] = managed_object['ConnectorVersion']
        info['ConnectionStatus'] = managed_object['ConnectionStatus']
        info['DeviceExternalIpAddress'] = managed_object['DeviceExternalIpAddress']
        info['ConnectionStatusLastChangeTime'] = managed_object['ConnectionStatusLastChangeTime']
        if info['ConnectionStatus'] == 'Connected':
            info['__Output']['ConnectionStatus'] = 'Green'
            info['Connected'] = True
        else:
            info['__Output']['ConnectionStatus'] = 'Red'
            info['Connected'] = False

        return info

    def create_target(self, serial_number, security_token):
        self.iobject = 'asset deviceclaim'
        create_attributes = ''
        create_attributes = '%s --SerialNumber %s' % (create_attributes, serial_number)
        create_attributes = '%s --SecurityToken %s' % (create_attributes, security_token)

        response = self.create(
            create_attributes,
            get_response=True,
            json_conversion=True
        )
        return response

    def delete_target(self, moid):
        self.iobject = 'asset deviceclaim'
        return self.delete(moid)
