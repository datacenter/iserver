from lib.xd.aci.contract.filter import AciContractFilter
from lib.xd.aci.contract.standard import AciContractStandard
from lib.xd.aci.contract.taboo import AciContractTaboo


class AciContract(
        AciContractFilter,
        AciContractStandard,
        AciContractTaboo
    ):
    def __init__(self):
        AciContractFilter.__init__(self)
        AciContractStandard.__init__(self)
        AciContractTaboo.__init__(self)

    def load_pre_aci_contract(self):
        if not self.load_pre_aci_contract_filter():
            return False

        if not self.load_pre_aci_contract_standard():
            return False

        if not self.load_pre_aci_contract_taboo():
            return False

        return True

    def prepare_aci_contract(self):
        self.my_output.debug('Get aci contract filter...')
        if not self.prepare_aci_contract_filter():
            self.my_output.error('Get aci contract filter failed')
            return False

        self.my_output.debug('Get aci contract standard...')
        if not self.prepare_aci_contract_standard():
            self.my_output.error('Get aci contract standard failed')
            return False

        self.my_output.debug('Get aci contract taboo...')
        if not self.prepare_aci_contract_taboo():
            self.my_output.error('Get aci contract taboo failed')
            return False

        return True

    def run_aci_contract(self):
        if not self.run_aci_contract_filter():
            return False

        if not self.run_aci_contract_standard():
            return False

        if not self.run_aci_contract_taboo():
            return False

        return True

    def load_post_aci_contract(self):
        if not self.load_post_aci_contract_filter():
            return False

        if not self.load_post_aci_contract_standard():
            return False

        if not self.load_post_aci_contract_taboo():
            return False

        return True

