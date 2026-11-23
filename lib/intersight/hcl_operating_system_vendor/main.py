from lib import output_helper
from lib.intersight.intersight_common import IntersightCommon


class HclOperatingSystemVendor(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'hcl operatingsystemvendor'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        self.my_output = None
        self.log_id = log_id

    def print(self, info, title=False):
        if self.my_output is None:
            self.my_output = output_helper.OutputHelper(log_id=self.log_id)

        if title:
            self.my_output.default(
                'Intersight OS Vendor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
                return

        order = [
            'Name'
        ]

        headers = [
            'Name'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
