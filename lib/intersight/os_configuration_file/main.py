from lib.intersight.intersight_common import IntersightCommon


class OsConfigurationFile(IntersightCommon):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'os configurationfile'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)

    def get_file_for_os(self, hcl_version_id):
        os_files = []
        items = self.get_all()
        if items is None:
            return os_files

        for item in items:
            match = False
            for distribution in item['Distributions']:
                if distribution['ObjectType'] == 'hcl.OperatingSystem' and distribution['Moid'] == hcl_version_id:
                    match = True
                    break
            if match:
                os_files.append(item)

        return os_files
