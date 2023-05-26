from lib.intersight.intersight_common import IntersightCommon


class ServerProfile(IntersightCommon):
    """Class for intersight server profile objects
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Action": "No-op",
        "ActionParams": [],
        "Ancestors": [],
        "AssignedServer": {
            "ClassId": "mo.MoRef",
            "Moid": "5fa04baa6176752d35cc0518",
            "ObjectType": "compute.RackUnit",
            "link": "https://www.intersight.com/api/v1/compute/RackUnits/5fa04baa6176752d35cc0518"
        },
        "AssociatedServer": null,
        "ClassId": "server.Profile",
        "ConfigChangeContext": {
            "ClassId": "policy.ConfigChangeContext",
            "ConfigChangeError": "",
            "ConfigChangeState": "Ok",
            "InitialConfigContext": {
            "ClassId": "policy.ConfigContext",
            "ConfigState": "",
            "ConfigType": "",
            "ControlAction": "",
            "ErrorState": "",
            "ObjectType": "policy.ConfigContext",
            "OperState": ""
            },
            "ObjectType": "policy.ConfigChangeContext"
        },
        "ConfigChangeDetails": [],
        "ConfigChanges": {
            "Changes": [],
            "ClassId": "policy.ConfigChange",
            "Disruptions": [],
            "ObjectType": "policy.ConfigChange"
        },
        "ConfigContext": {
            "ClassId": "policy.ConfigContext",
            "ConfigState": "Assigned",
            "ConfigType": "",
            "ControlAction": "No-op",
            "ErrorState": "",
            "ObjectType": "policy.ConfigContext",
            "OperState": "Ok"
        },
        "ConfigResult": {
            "ClassId": "mo.MoRef",
            "Moid": "6389df9277696e2d31f8b559",
            "ObjectType": "server.ConfigResult",
            "link": "https://www.intersight.com/api/v1/server/ConfigResults/6389df9277696e2d31f8b559"
        },
        "CreateTime": "2022-12-02T11:20:50.851Z",
        "Description": "",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "IsPmcDeployedSecurePassphraseSet": false,
        "ModTime": "2022-12-02T11:21:04.557Z",
        "Moid": "6389df9277696e2d31f8b557",
        "Name": "test2",
        "ObjectType": "server.Profile",
        "Organization": {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
        },
        "Owners": [
            "5be4b2ce67626c6d661ca38d"
        ],
        "PermissionResources": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            }
        ],
        "PolicyBucket": [],
        "ReservationReferences": [],
        "ResourceLease": {
            "ClassId": "mo.MoRef",
            "Moid": "6389df9f6962752d30868fc3",
            "ObjectType": "resourcepool.Lease",
            "link": "https://www.intersight.com/api/v1/resourcepool/Leases/6389df9f6962752d30868fc3"
        },
        "RunningWorkflows": [],
        "ServerAssignmentMode": "Static",
        "ServerPool": null,
        "SharedScope": "",
        "SrcTemplate": null,
        "StaticUuidAddress": "",
        "Tags": [],
        "TargetPlatform": "Standalone",
        "Type": "instance",
        "Uuid": "",
        "UuidAddressType": "NONE",
        "UuidLease": null,
        "UuidPool": null
    }
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'server profile'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def get_info(self, moid, cache=True):
        if cache:
            item = self.get_cache_moid(moid)
        else:
            item = self.get(moid)

        if item is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'Name',
            'ModTime',
            'Moid',
            'ServerAssignmentMode',
            'TargetPlatform',
            'Type'
        ]

        for key in keys:
            info[key] = item[key]

        info['ConfigState'] = item['ConfigContext']['ConfigState']
        info['ConfigChangeState'] = item['ConfigChangeContext']['ConfigChangeState']

        if info['ConfigState'].lower() == 'out-of-sync':
            info['__Output']['ConfigState'] = 'Red'

        if info['ConfigState'].lower() == 'assigned':
            info['__Output']['ConfigState'] = 'Yellow'

        if info['ConfigState'].lower() == 'validating':
            info['__Output']['ConfigState'] = 'Blue'

        if info['ConfigState'].lower() == 'associated':
            info['__Output']['ConfigState'] = 'Green'

        info['ConfigChangeDetails'] = []
        for config_change_details in item['ConfigChangeDetails']:
            config_change_info = {}
            config_change_info['EntityMoid'] = config_change_details['ConfigChangeContext']['EntityMoid']
            config_change_info['EntityType'] = config_change_details['ConfigChangeContext']['EntityType']
            info['ConfigChangeDetails'].append(
                config_change_info
            )

        return info
