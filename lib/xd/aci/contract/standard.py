import copy
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciContractStandard():
    def __init__(self):
        self.aci_contract_standard = None

    def load_pre_aci_contract_standard(self):
        self.aci_contract_standard = self.get_pre_cache('aci', 'standard')
        if self.aci_contract_standard is None:
            return False
        return True

    def set_post_aci_contract_standard(self):
        return self.set_post_cache('aci-standard', self.aci_contract_standard)

    def load_post_aci_contract_standard(self):
        self.aci_contract_standard = self.get_post_cache('aci-standard')
        if self.aci_contract_standard is None:
            return False
        return True

    def get_aci_contract_standard(self):
        info = copy.deepcopy(self.aci_contract_standard)
        return info

    def prepare_aci_contract_standard(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_contract_standard = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci contract standard: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_contract_standard:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-standard' % (aci_controller['name']))
                if cache is not None:
                    self.aci_contract_standard[aci_controller['name']] = cache
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

            apic_contract_standards = apic_handler.get_standard_contracts()
            if apic_contract_standards is None:
                continue

            self.aci_contract_standard[aci_controller['name']] = []
            for item in apic_contract_standards:
                item['apic'] = aci_controller['name']
                self.aci_contract_standard[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-standard' % (aci_controller['name']),
                self.aci_contract_standard[aci_controller['name']]
            )

        return True

    def run_aci_contract_standard(self):
        for key in self.aci_contract_standard:
            for item in self.aci_contract_standard[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra='standard'
                )

                for sub in item['vzFilter']:
                    sub['hash'] = aci_helper.get_aci_object_hash(
                        item['apic'],
                        sub,
                        extra='filter'
                    )

                item['filterCount'] = len(item['vzFilter'])
                item['subjectCount'] = len(item['vzSubj'])
                item['consumerCount'] = len(item['consumerEpg'])
                item['providerCount'] = len(item['providerEpg'])

                for sub in item['vzSubj']:
                    sub['filters'] = []
                    for fsub in sub['vzFilter']:
                        sub['filters'].append(
                            '%s/%s' % (
                                fsub['tenant'],
                                fsub['name']
                            )
                        )

        if not self.set_post_aci_contract_standard():
            return False

        return True
