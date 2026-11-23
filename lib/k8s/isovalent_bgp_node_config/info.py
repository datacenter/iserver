import time
from lib import filter_helper


class K8sIsovalentBGPNodeConfigInfo():
    def __init__(self):
        self.isovalent_bgp_node_config = None

    def get_isovalent_bgp_node_config_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['peer'] = []
        instances_mo = self.get(managed_object, 'status:bgpInstances', on_error=[], on_none=[])
        for instance_mo in instances_mo:
            peers_mo = self.get(instance_mo, 'peers', on_error=[], on_none=[])
            for peer_mo in peers_mo:
                peer_info = {}
                peer_info['__Output'] = {}
                peer_info['node'] = info['name']
                peer_info['instance'] = self.get(instance_mo, 'name')
                peer_info['local_asn'] = self.get(instance_mo, 'localASN')
                peer_info['name'] = self.get(peer_mo, 'name')
                peer_info['peer_asn'] = self.get(peer_mo, 'peerASN')
                peer_info['ip'] = self.get(peer_mo, 'peerAddress')
                peer_info['state'] = self.get(peer_mo, 'peeringState')
                if peer_info['state'] == 'established':
                    peer_info['__Output']['state'] = 'Green'
                else:
                    peer_info['__Output']['state'] = 'Red'
                peer_info['hold_time'] = self.get(peer_mo, 'timers:appliedHoldTimeSeconds')
                peer_info['keepalive_time'] = self.get(peer_mo, 'timers:appliedKeepaliveSeconds')
                peer_info['route'] = []
                routes_mo = self.get(peer_mo, 'routeCount', on_error=[], on_none=[])
                for route_mo in routes_mo:
                    route_info = {}
                    route_info['afi'] = self.get(route_mo, 'afi')
                    route_info['safi'] = self.get(route_mo, 'safi')
                    route_info['advertised'] = self.get(route_mo, 'advertised')
                    route_info['received'] = self.get(route_mo, 'received')
                    peer_info['route'].append(
                        route_info
                    )

                info['peer'].append(
                    peer_info
                )
                
        return info

    def get_isovalent_bgp_node_configs_info(self, cache_enabled=True):
        if cache_enabled:
            if self.isovalent_bgp_node_config is not None:
                return self.isovalent_bgp_node_config

        managed_objects = self.get_isovalent_bgp_node_config_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.isovalent_bgp_node_config = []
        for managed_object in managed_objects:
            isovalent_bgp_node_config_info = {}
            isovalent_bgp_node_config_info['info'] = self.get_isovalent_bgp_node_config_info(
                managed_object
            )
            isovalent_bgp_node_config_info['mo'] = managed_object
            self.isovalent_bgp_node_config.append(
                isovalent_bgp_node_config_info
            )

        return self.isovalent_bgp_node_config

    def match_isovalent_bgp_node_config(self, isovalent_bgp_node_config_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, isovalent_bgp_node_config_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_isovalent_bgp_node_config',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_isovalent_bgp_node_configs(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_isovalent_bgp_node_configs = self.get_isovalent_bgp_node_configs_info(cache_enabled=cache_enabled)
        if all_isovalent_bgp_node_configs is None:
            return None

        isovalent_bgp_node_configs = []

        for isovalent_bgp_node_config_info in all_isovalent_bgp_node_configs:
            if not self.match_isovalent_bgp_node_config(isovalent_bgp_node_config_info['info'], object_filter):
                continue

            if return_mo:
                isovalent_bgp_node_configs.append(
                    isovalent_bgp_node_config_info['mo']
                )
                continue

            isovalent_bgp_node_configs.append(
                isovalent_bgp_node_config_info['info']
            )

        return isovalent_bgp_node_configs

    def is_isovalent_bgp_node_config(self, name, cache_enabled=True):
        if self.get_isovalent_bgp_node_config(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_isovalent_bgp_node_config(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        isovalent_bgp_node_configs = self.get_isovalent_bgp_node_configs(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if isovalent_bgp_node_configs is None:
            return None

        if len(isovalent_bgp_node_configs) == 1:
            return isovalent_bgp_node_configs[0]

        return None

    def wait_isovalent_bgp_node_config(self, name, max_time=360):
        start_time = int(time.time())
        while True:
            node_config = self.get_isovalent_bgp_node_config(
                name,
                cache_enabled=False
            )
            if node_config is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_isovalent_bgp_node_config',
                    'Max time reached: %s' % (name)
                )
                return False

            time.sleep(5)
