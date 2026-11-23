from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.compute_server_setting.info import ComputeServerSettingInfo


class ComputeServerSetting(IntersightCommon, ComputeServerSettingInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'compute serversetting'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        ComputeServerSettingInfo.__init__(self)

    def set(self, attributes):
        create_iobject = 'compute updatecomputeserversetting'
        command = 'isctl create %s %s' % (create_iobject, attributes)
        response = self.isctl.create(command)
        return response
