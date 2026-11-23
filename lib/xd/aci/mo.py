import copy
from lib.aci import apic


class AciMo():
    def __init__(self):
        self.aci_mo = None

    def load_pre_aci_mo(self):
        self.aci_mo = self.get_pre_cache_2level('aci', 'mo')
        if self.aci_mo is None:
            return False
        return True

    def set_post_aci_mo(self):
        return self.set_post_cache('aci-mo', self.aci_mo)

    def load_post_aci_mo(self):
        self.aci_mo = self.get_post_cache('aci-mo')
        if self.aci_mo is None:
            return False
        return True

    def get_aci_mo(self):
        info = copy.deepcopy(self.aci_mo)
        return info

    def prepare_aci_mo(self, mos, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_mo = {}

        for aci_controller in aci_controllers:
            if aci_controller['name'] not in self.aci_mo:
                self.aci_mo[aci_controller['name']] = {}

            apic_handler = apic.Apic(
                aci_controller['ip'],
                aci_controller['port'],
                aci_controller['username'],
                aci_controller['password'],
                apic_name=aci_controller['name'],
                log_id=self.log_id
            )

            for mo in mos:
                self.my_output.debug('Aci mo: %s %s' % (aci_controller['name'], mo['key']))
                if cache_enabled and self.cache_ttl is not None:
                    # L2-cache
                    if aci_controller['name'] in self.aci_mo:
                        if mo['key'] in self.aci_mo[aci_controller['name']]:
                            self.my_output.debug('L2 Cache hit')
                            continue

                    # L3-cache
                    cache = self.get_cache('aci-%s-mo-%s' % (aci_controller['name'], mo['key']))
                    if cache is not None:
                        self.aci_mo[aci_controller['name']][mo['key']] = cache
                        self.my_output.debug('L3 Cache hit')
                        continue

                self.my_output.debug('Cache miss')

                managed_objects = None

                if mo['type'] == 'class':
                    managed_objects = apic_handler.get_class(
                        mo['name'],
                        query=mo['query'],
                        node_class=mo['node']
                    )

                if mo['type'] == 'dn':
                    managed_objects = apic_handler.get_managed_object(
                        mo['name'],
                        query=mo['query'],
                        node_class=mo['node']
                    )

                if managed_objects is None:
                    self.my_output.error('Failed to get mo class %s' % (mo['key']))
                    continue

                self.aci_mo[aci_controller['name']][mo['key']] = managed_objects['imdata']
                self.set_cache(
                    'aci-%s-mo-%s' % (aci_controller['name'], mo['key']),
                    self.aci_mo[aci_controller['name']][mo['key']]
                )

        return True

    def run_aci_mo(self):
        if not self.set_post_aci_mo():
            return False

        return True
