import json


class LinuxPvInfo():
    def __init__(self):
        self.pv = None

    def get_pv_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_pvs_info(self, cache_enabled=True):
        if cache_enabled and self.pv is not None:
            return self.pv

        try:
            pvs_mo = json.loads(
                self.get_pv_cmd(cache_enabled=cache_enabled)
            )['report'][0]['pv']
        except BaseException:
            self.log.error(
                'get_pvs_info',
                'Commands output parsing failed'
            )
            return None
        
        self.pv = []
        for pv_mo in pvs_mo:
            self.pv.append(
                self.get_pv_info(
                    pv_mo
                )
            )

        self.log.linux_mo(
            '%s.pv' % (self.server_display_name),
            self.pv
        )

        return self.pv
    
    def get_pvs(self, cache_enabled=True):
        pvs = self.get_pvs_info(cache_enabled=cache_enabled)
        return pvs
