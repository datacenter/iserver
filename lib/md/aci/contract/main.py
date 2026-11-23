from lib.md.aci.contract.filter import MdAciContractFilterOutput
from lib.md.aci.contract.standard import MdAciContractStandardOutput
from lib.md.aci.contract.taboo import MdAciContractTabooOutput

class MdAciContractOutput(
        MdAciContractFilterOutput,
        MdAciContractStandardOutput,
        MdAciContractTabooOutput
    ):
    def __init__(self):
        MdAciContractFilterOutput.__init__(self)
        MdAciContractStandardOutput.__init__(self)
        MdAciContractTabooOutput.__init__(self)

    def print_aci_contract_addon(self, consumed=None, provided=None, taboo=None, title=True):
        is_line = False
        if consumed is not None and len(consumed) > 0:
            is_line = True

        if consumed is not None and len(consumed) > 0:
            is_line = True

        if consumed is not None and len(consumed) > 0:
            is_line = True

        if not is_line:
            return

        if title:
            self.my_output.print_stream('## Contract', 'output')

        order = [
            'Contract Type',
            'Contract Tenant',
            'Contract Name'
        ]
        self.print_table_header(order)

        if consumed is not None:
            for contract in consumed:
                line = ''
                line = self.add_column(line, 'Consumed')
                line = self.add_column(line, contract['tenant'])
                line = self.add_column(line, contract['name'])
                self.my_output.print_stream(line, 'output')

        if provided is not None:
            for contract in provided:
                line = ''
                line = self.add_column(line, 'Provided')
                line = self.add_column(line, contract['tenant'])
                line = self.add_column(line, contract['name'])
                self.my_output.print_stream(line, 'output')

        if taboo is not None:
            for contract in taboo:
                line = ''
                line = self.add_column(line, 'Taboo')
                line = self.add_column(line, contract['tenant'])
                line = self.add_column(line, contract['name'])
                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')
