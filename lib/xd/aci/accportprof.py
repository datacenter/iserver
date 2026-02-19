import copy
from lib.aci import apic


class AciAccessPortProfile():
    def __init__(self):
        self.aci_accportprof = None

    def load_pre_aci_app(self):
        self.aci_accportprof = self.get_pre_cache('aci', 'accportprof')
        if self.aci_accportprof is None:
            return False
        return True

    def set_post_aci_app(self):
        return self.set_post_cache('aci-app', self.aci_accportprof)

    def load_post_aci_app(self):
        self.aci_accportprof = self.get_post_cache('aci-app')
        if self.aci_accportprof is None:
            return False
        return True

    def get_aci_accportprof(self, controller):
        info = copy.deepcopy(self.aci_accportprof[controller])
        return info

    def prepare_aci_accportprof(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_accportprof = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci accportprof: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_accportprof:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-accportprof' % (aci_controller['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit')
                    self.aci_accportprof[aci_controller['name']] = cache
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

            self.aci_accportprof[aci_controller['name']] = apic_handler.get_profiles_leaf_interface(
                node_interface_info=True,
                reln_info=True
            )

            self.set_cache(
                'aci-%s-accportprof' % (aci_controller['name']),
                self.aci_accportprof[aci_controller['name']]
            )

        return True

    def run_aci_accportprof(self):
        if not self.set_post_aci_app():
            return False

        return True
