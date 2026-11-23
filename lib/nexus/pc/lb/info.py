class PcLbInfo():
    def __init__(self):
        self.pc_lb = None

    def get_pc_lb_info(self, pc_lb_mo):
        if pc_lb_mo is None:
            return None


        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        keys = [
            'non-ip-val',
            'non-ip-sel',
            'ipv4-val',
            'ipv4-sel'
        ]
        for key in keys:
            info[key] = None
            if key in pc_lb_mo:
                info[key] = pc_lb_mo[key]

        info['module'] = []
        if 'TABLE_mod_configs' in pc_lb_mo:
            if 'ROW_mod_configs' in pc_lb_mo['TABLE_mod_configs']:
                if isinstance(pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs'], dict):
                    item = {}
                    item['id'] = pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']['mod-number']
                    item['non-ip-val'] = pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']['mod-non-ip-val']
                    item['non-ip-sel'] = pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']['mod-non-ip-sel']
                    item['ipv4-val'] = pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']['mod-ipv4-val']
                    item['ipv4-sel'] = pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']['mod-ipv4-sel']
                    info['module'].append(
                        item
                    )
                if isinstance(pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs'], list):
                    for item_mo in pc_lb_mo['TABLE_mod_configs']['ROW_mod_configs']:
                        item = {}
                        item['id'] = item_mo['mod-number']
                        item['non-ip-val'] = item_mo['mod-non-ip-val']
                        item['non-ip-sel'] = item_mo['mod-non-ip-sel']
                        item['ipv4-val'] = item_mo['mod-ipv4-val']
                        item['ipv4-sel'] = item_mo['mod-ipv4-sel']
                        info['module'].append(
                            item
                        )

        return info

    def get_pc_lb(self, cache_enabled=True):
        pc_lb_mo = self.get_pc_lb_mo(cache_enabled=cache_enabled)
        if pc_lb_mo is None:
            self.log.error(
                'get_pc_lb',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_pc_lb_info(pc_lb_mo)
