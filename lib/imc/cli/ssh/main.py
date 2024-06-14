import json


class ImcCliSsh():
    def __init__(self):
        self.ssh_mo = None

    def get_ssh_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ssh_mo is not None:
                return self.ssh_mo

            self.ssh_mo = self.get_icm_cli_cache_entry(
                'ssh'
            )
            if self.ssh_mo is not None:
                return self.ssh_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show ssh detail
        # SSH Settings:
        #     SSH Port: 22
        #     Timeout: 1800
        #     Max Sessions: 4
        #     Active Sessions: 1
        #     Enabled: yes

        self.ssh_mo = self.show_dict(
            'show ssh detail',
            start='SSH Settings:'
        )

        if self.ssh_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'ssh',
            self.ssh_mo
        )

        self.log.debug(
            'get_ssh_mo',
            json.dumps(self.ssh_mo, indent=4)
        )
        return self.ssh_mo

    def get_ssh_info(self, ssh_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in ssh_mo:
            info[key] = ssh_mo[key]

        self.log.debug(
            'get_ssh_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_ssh(self, cache_enabled=True):
        ssh_mo = self.get_ssh_mo(cache_enabled=cache_enabled)
        if ssh_mo is None:
            return None

        ssh_info = self.get_ssh_info(
            ssh_mo
        )

        return ssh_info
