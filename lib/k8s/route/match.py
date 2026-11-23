import time
from lib import filter_helper


class K8sRouteMatch():
    def __init__(self):
        pass

    def match_route(self, route_info, route_filter):
        if route_filter is None or len(route_filter) == 0:
            return True

        for ap_rule in route_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue
            
            if key == 'service':
                key_found = True
                if not filter_helper.match_string(value, route_info['service']):
                    return False                
                
            if not key_found:
                self.log.error(
                    'match_route',
                    'Unsupported key: %s' % (key)
                )

        return True