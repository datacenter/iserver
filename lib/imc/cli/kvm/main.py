import json


class ImcCliKvm():
    def __init__(self):
        self.kvm_mo = None

    def get_kvm_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.kvm_mo is not None:
                return self.kvm_mo

            self.kvm_mo = self.get_icm_cli_cache_entry(
                'kvm'
            )
            if self.kvm_mo is not None:
                return self.kvm_mo

        # comp-7-p2b-eu-spdc-WMP24040061# show kvm detail
        # KVM Settings:
        #     Max Sessions: 4
        #     Local Video: yes
        #     Active Sessions: 0
        #     Enabled: yes
        #     KVM Port: 2068

        self.kvm_mo = self.show_dict(
            'show kvm detail',
            start='KVM Settings:'
        )

        if self.kvm_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'kvm',
            self.kvm_mo
        )

        self.log.debug(
            'get_kvm_mo',
            json.dumps(self.kvm_mo, indent=4)
        )
        return self.kvm_mo

    def get_kvm_info(self, kvm_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in kvm_mo:
            info[key] = kvm_mo[key]

        self.log.debug(
            'get_kvm_info',
            json.dumps(info, indent=4)
        )
        return info

    def get_kvm(self, cache_enabled=True):
        kvm_mo = self.get_kvm_mo(cache_enabled=cache_enabled)
        if kvm_mo is None:
            return None

        kvm_info = self.get_kvm_info(
            kvm_mo
        )

        return kvm_info
