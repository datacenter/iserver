import copy
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciDomainAaa():
    def __init__(self):
        self.aci_domain_aaa = None

    def load_pre_aci_domain_aaa(self):
        self.aci_domain_aaa = self.get_pre_cache('aci', 'daaa')
        if self.aci_domain_aaa is None:
            return False
        return True

    def set_post_aci_domain_aaa(self):
        return self.set_post_cache('aci-daaa', self.aci_domain_aaa)

    def load_post_aci_domain_aaa(self):
        self.aci_domain_aaa = self.get_post_cache('aci-daaa')
        if self.aci_domain_aaa is None:
            return False
        return True

    def get_aci_domain_aaa(self):
        info = copy.deepcopy(self.aci_domain_aaa)
        return info

    def prepare_aci_domain_aaa(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_domain_aaa = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci domain aaa: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_domain_aaa:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-daaa' % (aci_controller['name']))
                if cache is not None:
                    self.aci_domain_aaa[aci_controller['name']] = cache
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

            apic_domains_aaa = apic_handler.get_domains_aaa()
            if apic_domains_aaa is None:
                continue

            self.aci_domain_aaa[aci_controller['name']] = []
            for item in apic_domains_aaa:
                item['apic'] = aci_controller['name']
                self.aci_domain_aaa[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-daaa' % (aci_controller['name']),
                self.aci_domain_aaa[aci_controller['name']]
            )

        return True

    def run_aci_domain_aaa(self):
        for key in self.aci_domain_aaa:
            for item in self.aci_domain_aaa[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra=self.get_aci_domain_type(
                        item['dn']
                    )
                )

        if not self.set_post_aci_domain_aaa():
            return False

        return True
