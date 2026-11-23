import json


class LinuxVgInfo():
    def __init__(self):
        self.vg = None

    def get_vg_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_vgs_info(self, cache_enabled=True):
        if cache_enabled and self.vg is not None:
            return self.vg

        try:
            vgs_mo = json.loads(
                self.get_vg_cmd(cache_enabled=cache_enabled)
            )['report'][0]['vg']
        except BaseException:
            self.log.error(
                'get_vgs_info',
                'Commands output parsing failed'
            )
            return None
        
        self.vg = []
        for vg_mo in vgs_mo:
            self.vg.append(
                self.get_vg_info(
                    vg_mo
                )
            )

        self.log.linux_mo(
            '%s.vg' % (self.server_display_name),
            self.vg
        )

        return self.vg
    
    def get_vgs(self, cache_enabled=True):
        vgs = self.get_vgs_info(cache_enabled=cache_enabled)
        return vgs
