import copy
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciContractTaboo():
    def __init__(self):
        self.aci_contract_taboo = None

    def load_pre_aci_contract_taboo(self):
        self.aci_contract_taboo = self.get_pre_cache('aci', 'taboo')
        if self.aci_contract_taboo is None:
            return False
        return True

    def set_post_aci_contract_taboo(self):
        return self.set_post_cache('aci-taboo', self.aci_contract_taboo)

    def load_post_aci_contract_taboo(self):
        self.aci_contract_taboo = self.get_post_cache('aci-taboo')
        if self.aci_contract_taboo is None:
            return False
        return True

    def get_aci_contract_taboo(self):
        info = copy.deepcopy(self.aci_contract_taboo)
        return info

    def prepare_aci_contract_taboo(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_contract_taboo = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci contract taboo: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_contract_taboo:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-taboo' % (aci_controller['name']))
                if cache is not None:
                    self.aci_contract_taboo[aci_controller['name']] = cache
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

            apic_contract_taboos = apic_handler.get_taboo_contracts()
            if apic_contract_taboos is None:
                continue

            self.aci_contract_taboo[aci_controller['name']] = []
            for item in apic_contract_taboos:
                item['apic'] = aci_controller['name']
                self.aci_contract_taboo[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-taboo' % (aci_controller['name']),
                self.aci_contract_taboo[aci_controller['name']]
            )

        return True

    def run_aci_contract_taboo(self):
        for key in self.aci_contract_taboo:
            for item in self.aci_contract_taboo[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra='taboo'
                )

                item['filterCount'] = len(item['vzFilter'])
                item['subjectCount'] = len(item['vzTSubj'])
                item['epgCount'] = len(item['protectedEpg'])

        if not self.set_post_aci_contract_taboo():
            return False

        return True
