from lib import log_helper


class BridgeDomainHealth():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_bridge_domain_health_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['score'] = managed_object['cur']
        score = int(info['score'])
        if score <= 50:
            info['__Output']['score'] = 'Red'

        if 50 < score <= 75:
            info['__Output']['score'] = 'Yellow'

        if score > 75:
            info['__Output']['score'] = 'Green'

        return info
