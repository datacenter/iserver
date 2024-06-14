import json


class ImcCliFault():
    def __init__(self):
        self.fault_mo = None
        self.fault_filter_mo = None
        self.fault_entry_mo = None

    def get_fault_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.fault_mo is not None:
                return self.fault_mo

            self.fault_mo = self.get_icm_cli_cache_entry(
                'fault'
            )
            if self.fault_mo is not None:
                return self.fault_mo

        # PEF Setting:
        #     Platform Event Enabled: yes

        self.fault_mo = self.show_dict(
            'show detail',
            start='PEF Settings:',
            scope='fault'
        )

        if self.fault_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'fault',
            self.fault_mo
        )

        self.log.debug(
            'get_fault_mo',
            json.dumps(self.fault_mo, indent=4)
        )
        return self.fault_mo

    def get_fault_filter_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.fault_filter_mo is not None:
                return self.fault_filter_mo

            self.fault_filter_mo = self.get_icm_cli_cache_entry(
                'fault_filter'
            )
            if self.fault_filter_mo is not None:
                return self.fault_filter_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /fault # show pef detail
        # Platform Event Filter 1:
        #     Event: Temperature Critical Assert Filter
        #     Action: none

        if keep_scope:
            self.fault_filter_mo = self.show_list(
                'show pef detail',
                'Platform Event Filter __INDEX__:',
                None,
                method='last word',
                top=False
            )
        else:
            self.fault_filter_mo = self.show_list(
                'show pef detail',
                'Platform Event Filter __INDEX__:',
                None,
                method='last word',
                scope='fault'
            )

        if self.fault_filter_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'fault_filter',
            self.fault_filter_mo
        )

        self.log.debug(
            'get_fault_filter_mo',
            json.dumps(self.fault_filter_mo, indent=4)
        )
        return self.fault_filter_mo

    def get_fault_entry_mo(self, keep_scope=False, cache_enabled=True):
        if cache_enabled:
            if self.fault_entry_mo is not None:
                return self.fault_entry_mo

            self.fault_entry_mo = self.get_icm_cli_cache_entry(
                'fault_entry'
            )
            if self.fault_entry_mo is not None:
                return self.fault_entry_mo

        # comp-7-p2b-eu-spdc-WMP24040061 /fault # show fault-entries detail
        # Fault Engine Log:
        #     Time: 2024-04-07T13:48:40
        #     Severity: info
        #     Fault DN: sys/rack-unit-1/mgmt/log-SEL-0/fault-F0462
        #     Code: F0462
        #     DN: sys/rack-unit-1/mgmt/log-SEL-0
        #     Cause: log-capacity
        #     Description: "CSCO_SEL_FULNESS: System Event log is Full: Clear the log"

        if keep_scope:
            self.fault_entry_mo = self.show_list(
                'show fault-entries detail',
                'Fault Engine Log:',
                None,
                method='last word',
                top=False
            )
        else:
            self.fault_entry_mo = self.show_list(
                'show fault-entries detail',
                'Fault Engine Log:',
                None,
                method='last word',
                scope='fault'
            )

        if self.fault_entry_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'fault_entry',
            self.fault_entry_mo
        )

        self.log.debug(
            'get_fault_entry_mo',
            json.dumps(self.fault_entry_mo, indent=4)
        )
        return self.fault_entry_mo

    def get_fault_info(self, fault_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in fault_mo:
            info[key] = fault_mo[key]

        return info

    def get_fault_filter_info(self, fault_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in fault_mo:
            info[key] = fault_mo[key]

        return info

    def get_fault_entry_info(self, fault_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in fault_mo:
            info[key] = fault_mo[key]

        return info

    def get_fault(self, cache_enabled=True):
        fault_mo = self.get_fault_mo(cache_enabled=cache_enabled)
        if fault_mo is None:
            return None

        fault_info = self.get_fault_info(
            fault_mo
        )

        fault_info['Platform Event Filter'] = []
        fault_filter_mo = self.get_fault_filter_mo(keep_scope=True, cache_enabled=cache_enabled)
        if fault_filter_mo is not None:
            for server_mo in fault_filter_mo:
                fault_info['Platform Event Filter'].append(
                    self.get_fault_filter_info(
                        server_mo
                    )
                )

        fault_info['Fault'] = []
        fault_entry_mo = self.get_fault_entry_mo(keep_scope=True, cache_enabled=cache_enabled)
        if fault_entry_mo is not None:
            for user_mo in fault_entry_mo:
                fault_info['Fault'].append(
                    self.get_fault_entry_info(
                        user_mo
                    )
                )

        self.log.debug(
            'get_fault_info',
            json.dumps(fault_info, indent=4)
        )

        return fault_info
