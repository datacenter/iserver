import copy
from lib.aci import apic
from lib.aci import helper as aci_helper


class AciSvi():
    def __init__(self):
        self.aci_svi = None

    def load_pre_aci_svi(self):
        self.aci_svi = self.get_pre_cache('aci', 'svi')
        if self.aci_svi is None:
            return False
        return True

    def set_post_aci_svi(self):
        return self.set_post_cache('aci-svi', self.aci_svi)

    def load_post_aci_svi(self):
        self.aci_svi = self.get_post_cache('aci-svi')
        if self.aci_svi is None:
            return False
        return True

    def get_aci_svi(self, controller, node_id):
        info = copy.deepcopy(self.aci_svi[controller][node_id])
        return info

    def prepare_aci_svi(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_svi = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci intf svi: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_svi:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-svi' % (aci_controller['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.aci_svi[aci_controller['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

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
                    'prepare_aci_svi',
                    'Failed to get nodes: %s' % (aci_controller['name'])
                )
                continue

            self.aci_svi[aci_controller['name']] = {}
            for node in nodes:
                interfaces = apic_handler.get_interfaces_svi(
                    node['podId'],
                    node['id']
                )
                self.aci_svi[aci_controller['name']][node['id']] = []
                if interfaces is not None:
                    for item in interfaces:
                        item['apic'] = aci_controller['name']
                        item['node_id'] = node['id']
                        self.aci_svi[aci_controller['name']][node['id']].append(
                            item
                        )

            self.set_cache(
                'aci-%s-svi' % (aci_controller['name']),
                self.aci_svi[aci_controller['name']]
            )

        return True

    def run_aci_svi(self):
        for controller_name in self.aci_svi:
            for node_id in self.aci_svi[controller_name]:
                for item in self.aci_svi[controller_name][node_id]:
                    item['hash'] = aci_helper.get_aci_interface_hash(
                        controller_name,
                        node_id,
                        item['id']
                    )

        if not self.set_post_aci_svi():
            return False

        return True
