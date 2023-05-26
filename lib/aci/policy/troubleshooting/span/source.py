from lib import log_helper


class PolicyTroubleshootingSpanSource():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_policy_troubleshooting_span_source_info(self, managed_object):
        keys = [
            'state',
            'tDn',
            'tRn'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info