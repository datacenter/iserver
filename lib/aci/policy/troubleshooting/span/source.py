class PolicyTroubleshootingSpanSource():
    def __init__(self):
        pass

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
