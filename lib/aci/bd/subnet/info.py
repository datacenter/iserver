from lib import ip_helper


class BridgeDomainSubnetInfo():
    def __init__(self):
        pass

    def get_subnet_usage(self, bridge_domain_subnets, endpoints):
        for subnet in bridge_domain_subnets:
            subnet['endpoints'] = 1
            if endpoints is not None:
                for endpoint in endpoints:
                    for endpoint_ip in endpoint['fvIp']:
                        if ip_helper.is_ipv4_in_cidr(endpoint_ip['addr'], subnet['network']):
                            subnet['endpoints'] = subnet['endpoints'] + 1

            subnet['usage'] = '%s/%s' % (
                subnet['endpoints'],
                subnet['size']
            )

            subnet['available'] = None
            if subnet['size'] is not None:
                subnet['available'] = subnet['size'] - subnet['endpoints']

        return bridge_domain_subnets

    def get_bridge_domain_subnet_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'ip',
            'ipDPLearning',
            'preferred',
            'rn',
            'scope',
            'virtual'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['preferred'] == 'yes':
            info['__Output']['preferred'] = 'Green'
            info['preferredTick'] = '\u2713'
        else:
            info['preferredTick'] = '\u2717'

        if info['virtual'] == 'yes':
            info['virtualTick'] = '\u2713'
        else:
            info['virtualTick'] = '\u2717'

        if info['ipDPLearning'] == 'enabled':
            info['ipDPLearningTick'] = '\u2713'
        else:
            info['ipDPLearningTick'] = '\u2717'

        info['network'] = '%s/%s' % (
            ip_helper.get_network_ipv4_in_cidr(info['ip']),
            info['ip'].split('/')[1]
        )
        info['gateway'] = info['ip'].split('/')[0]
        info['size'] = ip_helper.get_ipv4_cidr_size(info['ip'])

        return info
