import copy
from lib.aci import helper as aci_helper
from lib.aci import apic


class AciContractFilter():
    def __init__(self):
        self.aci_contract_filter = None

    def load_pre_aci_contract_filter(self):
        self.aci_contract_filter = self.get_pre_cache('aci', 'filter')
        if self.aci_contract_filter is None:
            return False
        return True

    def set_post_aci_contract_filter(self):
        return self.set_post_cache('aci-filter', self.aci_contract_filter)

    def load_post_aci_contract_filter(self):
        self.aci_contract_filter = self.get_post_cache('aci-filter')
        if self.aci_contract_filter is None:
            return False
        return True

    def get_aci_contract_filter(self):
        info = copy.deepcopy(self.aci_contract_filter)
        return info

    def prepare_aci_contract_filter(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_contract_filter = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci contract filter: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_contract_filter:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-filter' % (aci_controller['name']))
                if cache is not None:
                    self.aci_contract_filter[aci_controller['name']] = cache
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

            apic_contract_filters = apic_handler.get_contract_filters(
                usage_info=True
            )
            if apic_contract_filters is None:
                continue

            self.aci_contract_filter[aci_controller['name']] = []
            for item in apic_contract_filters:
                item['apic'] = aci_controller['name']
                self.aci_contract_filter[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-filter' % (aci_controller['name']),
                self.aci_contract_filter[aci_controller['name']]
            )

        return True

    def run_aci_contract_filter(self):
        for key in self.aci_contract_filter:
            for item in self.aci_contract_filter[key]:
                item['hash'] = aci_helper.get_aci_object_hash(
                    item['apic'],
                    item,
                    extra='filter'
                )

                item['entryCount'] = len(item['vzEntry'])
                item['standardCount'] = len(item['contract'])
                item['tabooCount'] = len(item['taboo'])

            self.aci_contract_filter[key] = sorted(
                self.aci_contract_filter[key],
                key=lambda i: (
                    i['tenant'].lower(),
                    i['name'].lower()
                )
            )

        if not self.set_post_aci_contract_filter():
            return False

        return True
