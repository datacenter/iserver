from lib.xd.aci.pool.vlan import AciPoolVlan


class AciPool(
        AciPoolVlan
    ):
    def __init__(self):
        AciPoolVlan.__init__(self)

    def load_pre_aci_pool(self):
        if not self.load_pre_aci_pool_vlan():
            return False

        return True

    def prepare_aci_pool(self):
        self.my_output.debug('Get aci pool vlan...')
        if not self.prepare_aci_pool_vlan():
            self.my_output.error('Get aci pool vlan failed')
            return False

        return True

    def run_aci_pool(self):
        if not self.run_aci_pool_vlan():
            return False

        return True

    def load_post_aci_pool(self):
        if not self.load_post_aci_pool_vlan():
            return False

        return True
