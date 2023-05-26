import copy

from lib.aci.contract.filter.output import FilterOutput
from lib.aci.contract.taboo.output import TabooOutput


class ContractOutput(FilterOutput, TabooOutput):
    def __init__(self):
        FilterOutput.__init__(self)
        TabooOutput.__init__(self)

    def print_contracts(self, info, show_contract_filters=False):
        self.my_output.default(
            'Standard Contracts',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'scope',
            'intent',
            'targetDscp',
            'vzFilter.subjectNameTenant',
            'vzFilter.nameTenant'
        ]

        headers = [
            'Contract',
            'Scope',
            'Intent',
            'Target DSCP',
            'Subject',
            'Filter'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vzFilter']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

        if show_contract_filters:
            filters_in_the_list = []
            filters = []
            for contract in info:
                for item in contract['vzFilter']:
                    if item['nameTenant'] not in filters_in_the_list:
                        filters_in_the_list.append(
                            item['nameTenant']
                        )
                        new_entry = copy.deepcopy(item)
                        filters.append(new_entry)

            self.print_filters(
                filters
            )

    def print_contracts_usage(self, info):
        self.my_output.default(
            'Standard Contracts Usage',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'consumerEpg.nameLong',
            'providerEpg.nameLong'
        ]

        headers = [
            'Contract',
            'Consumer EPG',
            'Provider EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['consumerEpg', 'providerEpg']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )
