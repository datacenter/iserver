import copy
from lib import ip_helper
from lib.aci import apic


class AciTenant():
    def __init__(self):
        self.aci_tenant = None

    def load_pre_aci_tenant(self):
        self.aci_tenant = self.get_pre_cache('aci', 'tenant')
        if self.aci_tenant is None:
            return False
        return True

    def set_post_aci_tenant(self):
        return self.set_post_cache('aci-tenant', self.aci_tenant)

    def load_post_aci_tenant(self):
        self.aci_tenant = self.get_post_cache('aci-tenant')
        if self.aci_tenant is None:
            return False
        return True

    def get_aci_tenant_names(self, controller):
        names = []

        if controller in self.aci_tenant:
            for item in self.aci_tenant[controller]:
                names.append(
                    item['name']
                )

        names = sorted(
            names,
            key=lambda i: i.lower()
        )
        return names

    def get_aci_tenant(self):
        info = copy.deepcopy(self.aci_tenant)
        return info

    def prepare_aci_tenant(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_tenant = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci tenant: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_tenant:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-tenant' % (aci_controller['name']))
                if cache is not None:
                    self.aci_tenant[aci_controller['name']] = cache
                    self.my_output.debug('L3 Cache hit')
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

            apic_tenants = apic_handler.get_tenants(
                count_info=True
            )
            if apic_tenants is None:
                continue

            self.aci_tenant[aci_controller['name']] = []
            for item in apic_tenants:
                item['apic'] = aci_controller['name']
                self.aci_tenant[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-tenant' % (aci_controller['name']),
                self.aci_tenant[aci_controller['name']]
            )

        return True

    def run_aci_tenant(self):
        for key in self.aci_tenant:
            for item in self.aci_tenant[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['name']
                    )
                )

        if not self.set_post_aci_tenant():
            return False

        return True
