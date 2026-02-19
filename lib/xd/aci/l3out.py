import copy
from lib import ip_helper
from lib.aci import apic


class AciL3Out():
    def __init__(self):
        self.aci_l3out = None

    def load_pre_aci_l3out(self):
        self.aci_l3out = self.get_pre_cache('aci', 'l3out')
        if self.aci_l3out is None:
            return False
        return True

    def set_post_aci_l3out(self):
        return self.set_post_cache('aci-l3out', self.aci_l3out)

    def load_post_aci_l3out(self):
        self.aci_l3out = self.get_post_cache('aci-l3out')
        if self.aci_l3out is None:
            return False
        return True

    def get_aci_l3out(self):
        info = copy.deepcopy(self.aci_l3out)
        return info

    def prepare_aci_l3out(self, cache_enabled=True):
        aci_controllers = self.get_aci_handlers()
        if aci_controllers is None or len(aci_controllers) == 0:
            return False

        self.aci_l3out = {}

        for aci_controller in aci_controllers:
            self.my_output.debug('Aci l3out: %s' % (aci_controller['name']))
            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if aci_controller['name'] in self.aci_l3out:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('aci-%s-l3out' % (aci_controller['name']))
                if cache is not None:
                    self.aci_l3out[aci_controller['name']] = cache
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

            apic_l3outs = apic_handler.get_l3outs()
            if apic_l3outs is None:
                continue

            self.aci_l3out[aci_controller['name']] = []
            for item in apic_l3outs:
                item['apic'] = aci_controller['name']
                self.aci_l3out[aci_controller['name']].append(
                    item
                )

            self.set_cache(
                'aci-%s-l3out' % (aci_controller['name']),
                self.aci_l3out[aci_controller['name']]
            )

        return True

    def run_aci_l3out(self):
        for key in self.aci_l3out:
            for item in self.aci_l3out[key]:
                item['hash'] = ip_helper.get_string_md5(
                    '%s %s' % (
                        item['apic'],
                        item['nameTenant']
                    )
                )

                item['extEpgCount'] = len(item['l3extInstP'])
                item['lnpCount'] = len(item['logicalNodeProfile'])
                item['nodeCount'] = len(item['configured_node'])

        if not self.set_post_aci_l3out():
            return False

        return True
