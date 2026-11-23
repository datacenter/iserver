import copy
from lib.aci import apic


class AciBgp():
    def __init__(self):
        self.aci_bgp = None

    def load_pre_aci_bgp(self):
        self.aci_bgp = self.get_pre_cache('aci', 'bgp')
        if self.aci_bgp is None:
            return False
        return True

    def set_post_aci_bgp(self):
        return self.set_post_cache('aci-bgp', self.aci_bgp)

    def load_post_aci_bgp(self):
        self.aci_bgp = self.get_post_cache('aci-bgp')
        if self.aci_bgp is None:
            return False
        return True

    def get_aci_bgp(self):
        info = copy.deepcopy(self.aci_bgp)
        return info

    def prepare_aci_bgp(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_bgp = {}

        for aci_controller in aci_controllers:
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_bgp:
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-bgp' % (aci_controller['name']))
                if cache is not None:
                    self.aci_bgp[aci_controller['name']] = cache
                    continue

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            nodes = apic_handler.get_nodes(
                node_filter=['role:!controller']
            )
            if nodes is None:
                self.log.error(
                    'prepare_aci_bgp',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_bgp[aci_controller['name']] = {}
            for node in nodes:
                self.aci_bgp[aci_controller['name']][node['id']] = apic_handler.get_protocol_bgp(
                    node['podId'],
                    node['id'],
                    instance_info=True,
                    domain_info=True,
                    neighbor_info=True,
                    stats_info=True,
                    prefix_info=True
                )

            self.set_cache(
                'aci-%s-bgp' % (aci_controller['name']),
                self.aci_bgp[aci_controller['name']]
            )

        return True

    def run_aci_bgp(self):
        if not self.set_post_aci_bgp():
            return False

        return True
