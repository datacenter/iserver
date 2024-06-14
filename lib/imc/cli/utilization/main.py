import json


class ImcCliUtilization():
    def __init__(self):
        self.utilization_mo = None

    def get_utilization_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.utilization_mo is not None:
                return self.utilization_mo

            self.utilization_mo = self.get_icm_cli_cache_entry(
                'utilization'
            )
            if self.utilization_mo is not None:
                return self.utilization_mo

        # CPU Utilization (%): 3
        # Memory Utilization (%): 2
        # I/O Utilization (%): 0
        # Overall Utilization (%): 3

        self.utilization_mo = self.show_dict(
            'show cups-utilization detail',
            scope='chassis'
        )

        if self.utilization_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'utilization',
            self.utilization_mo
        )

        self.log.debug(
            'get_utilization_mo',
            json.dumps(self.utilization_mo, indent=4)
        )
        return self.utilization_mo

    def get_utilization_info(self, utilization_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in utilization_mo:
            info[key] = utilization_mo[key]

        self.log.debug(
            'get_utilization_mo',
            json.dumps(info, indent=4)
        )
        return info

    def get_utilization(self, cache_enabled=True):
        utilization_mo = self.get_utilization_mo(cache_enabled=cache_enabled)
        if utilization_mo is None:
            return None

        utilization_info = self.get_utilization_info(
            utilization_mo
        )

        return utilization_info
