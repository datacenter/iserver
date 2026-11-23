class PolicyMonitoring():
    def __init__(self):
        pass

    def get_policy_monitoring_info(self, managed_object):
        keys = [
            'state',
            'tDn',
            'tRn',
            'tnMonInfraPolName'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['name'] = info['tRn'].split('moninfra-')[1]

        return info
