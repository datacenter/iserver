from lib import output_helper

from lib.intersight.intersight_common import IntersightCommon


class HclOperatingSystemVendor(IntersightCommon):
    """Class for intersight hcl operating system vendor objects

    {
        "AccountMoid": "",
        "Ancestors": [],
        "ClassId": "hcl.OperatingSystemVendor",
        "CreateTime": "2018-08-15T00:16:49.873Z",
        "DomainGroupMoid": "SystemDomainGroup",
        "ModTime": "2018-08-15T00:16:49.886Z",
        "Moid": "5b7370f16836726e35cc7028",
        "Name": "Microsoft",
        "ObjectType": "hcl.OperatingSystemVendor",
        "Owners": [
            "system"
        ],
        "SharedScope": "",
        "Tags": []
    }
    """
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'hcl operatingsystemvendor'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.log_id = log_id
        self.my_output = None

    def print(self, vendors):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(log_id=self.log_id)

        sorted_vendors = sorted(vendors, key=lambda i: i['Name'])

        order = [
            'Moid',
            'Name'
        ]
        headers = [
            'Moid',
            'Name'
        ]
        self.my_output.my_table(
            sorted_vendors,
            order=order,
            headers=headers,
            table=True
        )
