import json


class ImcCliHdd():
    def __init__(self):
        self.hdd_mo = None
        self.hdd_pid_mo = None

    def get_hdd_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.hdd_mo is not None:
                return self.hdd_mo

            self.hdd_mo = self.get_icm_cli_cache_entry(
                'hdd'
            )
            if self.hdd_mo is not None:
                return self.hdd_mo

        # Name HDD1_STATUS:
        #     Status : absent
        #     LocateLEDStatus : TurnOFF

        self.hdd_mo = self.show_list(
            'show hdd detail',
            'Name',
            'Name',
            method='last word',
            scope='chassis'
        )

        if self.hdd_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'hdd',
            self.hdd_mo
        )

        self.log.debug(
            'get_hdd_mo',
            json.dumps(self.hdd_mo, indent=4)
        )
        return self.hdd_mo

    def get_hdd_pid_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.hdd_pid_mo is not None:
                return self.hdd_pid_mo

            self.hdd_pid_mo = self.get_icm_cli_cache_entry(
                'hdd_pid'
            )
            if self.hdd_pid_mo is not None:
                return self.hdd_pid_mo

        # Disk 3:
        #     Controller: MRAID
        #     Description: 1.2TB 12G SAS 10K RPM SFF HDD
        #     Product ID: UCS-HD12TB10K12N
        #     Vendor: TOSHIBA
        #     Model: AL15SEB120N
        #     SerialNumber: Z820A08VFJRG

        self.hdd_pid_mo = self.show_list(
            'show hdd-pid detail',
            'Disk',
            'Id',
            method='last word',
            scope='chassis'
        )

        if self.hdd_pid_mo is None:
            return None

        self.set_imc_cli_cache_entry(
            'hdd_pid',
            self.hdd_pid_mo
        )

        self.log.debug(
            'get_hdd_pid_mo',
            json.dumps(self.hdd_pid_mo, indent=4)
        )
        return self.hdd_pid_mo

    def get_hdd_info(self, hdd_mo):
        info = {}
        info['__Output'] = {}
        info['__IP'] = self.endpoint_ip

        for key in hdd_mo:
            info[key] = hdd_mo[key]

        info['Name'] = info['Name'].split('_STATUS')[0]
        info['Id'] = info['Name'].split('HDD')[1]

        if 'Operability' in info:
            if info['Operability'] == 'Operable':
                info['__Output']['Operability'] = 'Green'
            else:
                info['__Output']['Operability'] = 'Red'

        info['__Key'] = 'Name'
        info['__Value'] = info[info['__Key']]

        return info

    def get_hdd_pid_info(self, hdd_mo):
        info = {}
        for key in hdd_mo:
            info[key] = hdd_mo[key]
        return info

    def get_hdd(self, cache_enabled=True):
        hdds_mo = self.get_hdd_mo(cache_enabled=cache_enabled)
        if hdds_mo is None:
            return None

        hdds_pid_mo = self.get_hdd_pid_mo(cache_enabled=cache_enabled)
        if hdds_pid_mo is None:
            return None

        hdds_info = []

        for hdd_mo in hdds_mo:
            hdds_info.append(
                self.get_hdd_info(
                    hdd_mo
                )
            )

        keys = [
            'Controller',
            'Description',
            'Product ID',
            'Vendor',
            'Model',
            'SerialNumber'
        ]
        for hdd_info in hdds_info:
            for key in keys:
                hdd_info[key] = ''

        for hdd_pid_mo in hdds_pid_mo:
            hdd_pid_info = self.get_hdd_pid_info(
                hdd_pid_mo
            )
            for hdd_info in hdds_info:
                if hdd_info['Id'] == hdd_pid_info['Id']:
                    for key in keys:
                        hdd_info[key] = hdd_pid_info[key]

        self.log.debug(
            'get_hdd_info',
            json.dumps(hdds_info, indent=4)
        )

        return hdds_info
