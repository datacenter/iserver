class BridgeDomainHealthInfo():
    def __init__(self):
        pass

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
