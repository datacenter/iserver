import re
import traceback

from lib.intersight.intersight_common import IntersightCommon


class Organization(IntersightCommon):
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
