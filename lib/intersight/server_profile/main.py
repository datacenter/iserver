from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.server_profile.info import ServerProfileInfo


class ServerProfile(IntersightCommon, ServerProfileInfo):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'server profile'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)
        ServerProfileInfo.__init__(self)
