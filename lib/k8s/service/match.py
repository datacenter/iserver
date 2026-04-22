from lib import filter_helper
from lib import ip_helper


class K8sServiceMatch():
    def __init__(self):
        pass

    def match_service(self, service_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue
            
            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, service_info['owner']):
                    return False

            if key == 'type':
                key_found = True
                if not filter_helper.match_string(value, service_info['type']):
                    return False

            if key == 'cluster-ip':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if cluster_ip == value:
                        value_match = True

                if not value_match:
                    return False

            if key == 'cluster-subnet':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if ip_helper.is_ipv4_in_cidr(cluster_ip, value):
                        value_match = True

                if not value_match:
                    return False

            if key == 'cluster-string':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if filter_helper.match_string(cluster_ip, value):
                        value_match = True

            if key == 'external-ip':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if external_ip == value:
                        value_match = True

                if not value_match:
                    return False

            if key == 'external-subnet':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if ip_helper.is_ipv4_in_cidr(external_ip, value):
                        value_match = True

                if not value_match:
                    return False

            if key == 'external-string':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if filter_helper.match_string(external_ip, value):
                        value_match = True

                if filter_helper.match_string(value, service_info['external_name']):
                    value_match = True

                if not value_match:
                    return False

            if key == 'port':
                key_found = True
                value_match = False
                for port in service_info['port']:
                    if filter_helper.match_integer(value, port['port']):
                        value_match = True

                if not value_match:
                    return False

            if key == 'special':
                key_found = True
                if not filter_helper.match_string(value, service_info['special']):
                    return False

            if key == 'selector':
                key_found = True
                (selector_key, selector_value) = value.split(':')
                if selector_key not in service_info['selector']:
                    return False

                if not filter_helper.match_string(selector_value, service_info['selector'][selector_key]):
                    return False

            if not key_found:
                self.log.error(
                    'match_service',
                    'Unsupported key: %s' % (key)
                )

        return True