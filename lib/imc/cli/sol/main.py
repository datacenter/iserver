import json


class ImcCliSol():
    def __init__(self):
        self.sol_mo = None

    def get_sol_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sol_mo is not None:
                return self.sol_mo

            self.sol_mo = self.get_icm_cli_cache_entry(
                'sol'
            )
            if self.sol_mo is not None:
                return self.sol_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show sol detail
        # Serial Over LAN:
        #     Enabled: yes
        #     Baud Rate(bps): 115200
        #     Com Port: com0
        #     SOL SSH Port: 2400

        self.sol_mo = self.show_dict(
            'show sol detail',
            start='Serial Over LAN:'
        )

        if self.sol_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'sol',
            self.sol_mo
        )

        self.log.debug(
            'get_sol_mo',
            json.dumps(self.sol_mo, indent=4)
        )
        return self.sol_mo

    def get_sol_info(self, sol_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in sol_mo:
            info[key] = sol_mo[key]

        self.log.debug(
            'get_sol_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_sol(self, cache_enabled=True):
        sol_mo = self.get_sol_mo(cache_enabled=cache_enabled)
        if sol_mo is None:
            return None

        sol_info = self.get_sol_info(
            sol_mo
        )

        return sol_info
