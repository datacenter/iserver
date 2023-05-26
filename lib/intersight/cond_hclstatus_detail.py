from lib.intersight.intersight_common import IntersightCommon


class CondHclStatusDetail(IntersightCommon):
    """Class for intersight cond hcl status detail
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5e8c4ed773736f2d31815ce0",
                "ObjectType": "cond.HclStatus",
                "link": "https://www.intersight.com/api/v1/cond/HclStatuses/5e8c4ed773736f2d31815ce0"
            }
        ],
        "ClassId": "cond.HclStatusDetail",
        "Component": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4fec6176752d32d62e0b",
            "ObjectType": "storage.Controller",
            "link": "https://www.intersight.com/api/v1/storage/Controllers/5e8c4fec6176752d32d62e0b"
        },
        "CreateTime": "2020-04-07T10:03:29.535Z",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "HardwareStatus": "Not-Evaluated",
        "HclCimcVersion": "4.1(2)",
        "HclDriverName": "",
        "HclDriverVersion": "",
        "HclFirmwareVersion": "24.12.1-0456",
        "HclModel": "Cisco 12G SAS Modular Raid Controller",
        "HclStatus": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed773736f2d31815ce0",
            "ObjectType": "cond.HclStatus",
            "link": "https://www.intersight.com/api/v1/cond/HclStatuses/5e8c4ed773736f2d31815ce0"
        },
        "InvCimcVersion": "4.1(2f)",
        "InvDriverName": "",
        "InvDriverVersion": "",
        "InvFirmwareVersion": "24.12.1-0456",
        "InvModel": "Cisco 12G SAS Modular Raid Controller",
        "ModTime": "2022-05-09T13:35:25.208Z",
        "Moid": "5e8c4ff173736f2d3181b134",
        "ObjectType": "cond.HclStatusDetail",
        "Owners": [
            "5be4b2ce67626c6d661ca38d",
            "5e8c4ecd6f72612d302b11a6"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5e8c4ed773736f2d31815ce0",
            "ObjectType": "cond.HclStatus",
            "link": "https://www.intersight.com/api/v1/cond/HclStatuses/5e8c4ed773736f2d31815ce0"
        },
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
        "Reason": "Missing-Os-Driver-Info",
        "SharedScope": "",
        "SoftwareStatus": "Not-Evaluated",
        "Status": "Incomplete",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'cond hclstatusdetail'
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

        keys = [
            'HardwareStatus',
            'HclCimcVersion',
            'HclDriverName',
            'HclDriverVersion',
            'HclFirmwareVersion',
            'HclModel',
            'Reason',
            'SoftwareStatus',
            'Status',
            'Moid'
        ]

        for key in keys:
            if key in item:
                info[key] = item[key]

        for key in ['Status', 'SoftwareStatus', 'HardwareStatus']:
            if key in info:
                if info[key] == 'Incomplete':
                    info['__Output'][key] = 'Red'

                if info[key] == 'Not-Listed':
                    info['__Output'][key] = 'Yellow'

                if info[key] == 'Validated':
                    info['__Output'][key] = 'Green'

                if info[key] == 'Not-Evaluated':
                    info['__Output'][key] = 'Yellow'

        return info
