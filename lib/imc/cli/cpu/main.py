import json


class ImcCliCpu():
    def __init__(self):
        self.cpu_mo = None
        self.cpu_pid_mo = None

    def get_cpu_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cpu_mo is not None:
                return self.cpu_mo

            self.cpu_mo = self.get_icm_cli_cache_entry(
                'cpu'
            )
            if self.cpu_mo is not None:
                return self.cpu_mo

        # Name CPU1:
        #     Manufacturer: Intel(R) Corporation
        #     Family: Xeon
        #     Thread Count : 40
        #     Cores : 20
        #     Version: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
        #     Speed (Mhz) : 2500
        #     Signature: Type 0, Family 6, Model 85, Stepping 7
        #     Status: Enabled
        # Name CPU2:
        #     Manufacturer: Intel(R) Corporation
        #     Family: Xeon
        #     Thread Count : 40
        #     Cores : 20
        #     Version: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
        #     Speed (Mhz) : 2500
        #     Signature: Type 0, Family 6, Model 85, Stepping 7
        #     Status: Enabled


        self.cpu_mo = self.show_list(
            'show cpu detail',
            'Name',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.cpu_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'cpu',
            self.cpu_mo
        )

        self.log.debug(
            'get_cpu_mo',
            json.dumps(self.cpu_mo, indent=4)
        )
        return self.cpu_mo

    def get_cpu_pid_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.cpu_pid_mo is not None:
                return self.cpu_pid_mo

            self.cpu_pid_mo = self.get_icm_cli_cache_entry(
                'cpu_pid'
            )
            if self.cpu_pid_mo is not None:
                return self.cpu_pid_mo

        # Socket CPU1:
        #     Description: Intel(R) Xeon(R) Gold 6248 2.50 GHz 150W 20C 27.50MB Cache DDR4 2933MHz 1TB
        #     Product ID: UCS-CPU-I6248
        #     Model: Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz
        #     Signature: Type 0, Family 6, Model 85, Stepping 7
        #     Current Speed: 2500
        #     Status: Enabled

        self.cpu_pid_mo = self.show_list(
            'show cpu-pid detail',
            'Socket',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.cpu_pid_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'cpu_pid',
            self.cpu_pid_mo
        )

        self.log.debug(
            'get_cpu_pid_mo',
            json.dumps(self.cpu_pid_mo, indent=4)
        )
        return self.cpu_pid_mo

    def get_cpu_info(self, cpu_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in cpu_mo:
            info[key] = cpu_mo[key]

        if 'Status' in info:
            if info['Status'] == 'Enabled':
                info['__Output']['Status'] = 'Green'
            else:
                info['__Output']['Status'] = 'Red'

        info['__Key'] = 'Name'
        info['__Value'] = info[info['__Key']]

        return info

    def get_cpu_pid_info(self, cpu_mo):
        info = {}
        for key in cpu_mo:
            info[key] = cpu_mo[key]
        return info

    def get_cpu(self, cache_enabled=True):
        cpus_mo = self.get_cpu_mo(cache_enabled=cache_enabled)
        if cpus_mo is None:
            return None

        cpus_pid_mo = self.get_cpu_pid_mo(cache_enabled=cache_enabled)
        if cpus_pid_mo is None:
            return None

        cpus_info = []

        for cpu_mo in cpus_mo:
            cpus_info.append(
                self.get_cpu_info(
                    cpu_mo
                )
            )

        keys = [
            'Description',
            'Product ID',
            'Model'
        ]
        for cpu_info in cpus_info:
            for key in keys:
                cpu_info[key] = 'NA'

        for cpu_pid_mo in cpus_pid_mo:
            cpu_pid_info = self.get_cpu_pid_info(
                cpu_pid_mo
            )
            for cpu_info in cpus_info:
                if cpu_info['Name'] == cpu_pid_info['Name']:
                    for key in keys:
                        cpu_info[key] = cpu_pid_info[key]

        self.log.debug(
            'get_cpu_info',
            json.dumps(cpus_info, indent=4)
        )

        return cpus_info
