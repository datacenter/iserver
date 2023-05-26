import re
import traceback

from lib.intersight.intersight_common import IntersightCommon


class Organization(IntersightCommon):
    """Class for intersight organization objects

    {
        "Account": {
            "ClassId": "mo.MoRef",
            "Moid": "5be4b2ce67626c6d661ca38d",
            "ObjectType": "iam.Account",
            "link": "https://www.intersight.com/api/v1/iam/Accounts/5be4b2ce67626c6d661ca38d"
        },
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [],
        "ClassId": "organization.Organization",
        "CreateTime": "2019-12-09T10:09:55.507Z",
        "Description": "EMEAR Service Provider DC Specialists",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "ModTime": "2020-11-02T17:27:23.443Z",
        "Moid": "5dee1d736972652d321d26b5",
        "Name": "EMEAR-SPDC-Specialists",
        "ObjectType": "organization.Organization",
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
        "ResourceGroups": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d716972652d321d269f",
            "ObjectType": "resource.Group",
            "link": "https://www.intersight.com/api/v1/resource/Groups/5dee1d716972652d321d269f"
        }
        ],
        "SharedScope": "",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'organization organization'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def filter(self, tag=None, name=None, name_pattern=None, details=True):
        filtered = []
        try:
            response = IntersightCommon.get_all(self)
            if response is None:
                self.log.error('organization.filter', 'Possible bug on get all')
                return filtered

            for item in response:
                if tag is not None:
                    if tag not in item['Tags']:
                        continue

                if name is not None:
                    if item['Name'] != name:
                        continue

                if name_pattern is not None:
                    if not re.match(name_pattern, item['Name']):
                        continue

                if details:
                    filtered.append(item)
                else:
                    filtered.append(item['Moid'])

        except BaseException:
            self.log.error('organization.filter', traceback.format_exc())
            return None

        return filtered
