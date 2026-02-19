import copy
from lib import ip_helper
from lib.vc import vcenter


class VcNetwork():
    def __init__(self):
        self.vc_network = None

    def load_pre_vc_network(self):
        self.vc_network = self.get_pre_cache('vcenter', 'network')
        if self.vc_network is None:
            return False

        return True

    def set_post_vc_network(self):
        return self.set_post_cache('vcenter-network', self.vc_network)

    def load_post_vc_network(self):
        self.vc_network = self.get_post_cache('vcenter-network')
        if self.vc_network is None:
            return False

        return True

    def get_vc_network(self, vc):
        if vc in self.vc_network:
            info = copy.deepcopy(self.vc_network[vc])
            return info

        return None

    def get_vc_network_by_name(self, vc, network_name):
        if vc not in self.vc_network:
            return None

        for network in self.vc_network[vc]:
            if network['name'] == network_name:
                return network

        return None

    def prepare_vc_networks(self, cache_enabled=True):
        vc_instances = self.get_vc_handlers()
        if vc_instances is None or len(vc_instances) == 0:
            return False

        self.vc_network = {}

        for vc_instance in vc_instances:
            self.my_output.debug('Vcenter networks: %s' % (vc_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if vc_instance['name'] in self.vc_network:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('vcenter-%s-network' % (vc_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.vc_network[vc_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            vc_handler = vcenter.Vcenter(
                vc_instance['ip'],
                vc_instance['username'],
                vc_instance['password'],
                port=vc_instance['port'],
                log_id=self.log_id
            )

            self.vc_network[vc_instance['name']] = vc_handler.get_networks()
            if self.vc_network[vc_instance['name']] is None:
                return False

            self.set_cache(
                'vcenter-%s-network' % (vc_instance['name']),
                self.vc_network[vc_instance['name']]
            )

        return True

    def run_vc_network_independent(self):
        for vc in self.vc_instance:
            if vc not in self.vc_network:
                self.vc_network[vc] = []

            for network in self.vc_network[vc]:
                network['_name'] = network['name']

                network['up'] = False
                if network['overallStatus'] == 'green' and network['accessible']:
                    network['up'] = True

                if len(network['name'].split('-DVUplinks-')) == 2:
                    network['uplink'] = True
                else:
                    network['uplink'] = False

                network['_type'] = None
                if network['type'] == 'standard':
                    network['_type'] = 'Standard network'
                if network['type'] == 'dvs':
                    if network['uplink']:
                        network['_type'] = 'Uplink port group'
                    else:
                        network['_type'] = 'Distributed port group'

                network['vmUp'] = []
                for vm_name in network['vm']:
                    for vm in self.vc_vm[vc]:
                        if vm['name'] == vm_name:
                            if self.is_vc_vm_up(vm):
                                network['vmUp'].append(
                                    vm_name
                                )

                network['numVms'] = len(network['vm'])
                network['numVmsUp'] = len(network['vmUp'])
                network['numHosts'] = len(network['host'])
                if 'ports' not in network:
                    network['ports'] = []
                if 'numPorts' not in network:
                    network['numPorts'] = 0
                if 'vlans' not in network:
                    network['vlans'] = []

                if 'portGroupKey' not in network:
                    network['portGroupKey'] = None

                network['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        vc,
                        network['name']
                    )
                )

            self.vc_network[vc] = sorted(
                self.vc_network[vc],
                key=lambda i: i['name'].lower()
            )

        return True

    def run_vc_network_xd(self):
        for vc in self.vc_network:
            for network in self.vc_network[vc]:
                network['numHostsUp'] = 0
                for host in self.vc_host[vc]:
                    if host['name'] in network['host']:
                        if host['up']:
                            network['numHostsUp'] += 1

                if not network['uplink'] and network['type'] == 'dvs':
                    network['portsUp'] = []
                    network['numPortsUp'] = 0
                    for dvs in self.vc_dvs[vc]:
                        for port in dvs['port']:
                            if port['key'] in network['ports']:
                                if port['linkUp'] is not None and port['linkUp']:
                                    network['numPortsUp'] += 1
                                    network['portsUp'].append(
                                        port['key']
                                    )

                if network['uplink'] and network['type'] == 'dvs':
                    network['portsUp'] = []
                    network['numPortsUp'] = 0
                    for dvs in self.vc_dvs[vc]:
                        for port in dvs['port']:
                            if port['key'] in network['ports']:
                                if port['linkUp'] is not None and port['linkUp']:
                                    network['numPortsUp'] += 1
                                    network['portsUp'].append(
                                        port['key']
                                    )

        if not self.set_post_vc_network():
            return False

        return True
