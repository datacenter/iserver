class PcStateInfo():
    def __init__(self):
        self.pc_state = None

    def get_pc_state_info(self, pc_state_mo):
        if pc_state_mo is None:
            return None

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        self.pc_state = []
        if len(pc_state_mo) > 0:
            for managed_object in pc_state_mo['TABLE_channel']['ROW_channel']:
                info = {}
                info['__Output'] = {}
                info['nexus_name'] = self.nexus_name

                keys = [
                    'group',
                    'port-channel',
                    'layer',
                    'status',
                    'type',
                    'prtcl'
                ]
                for key in keys:
                    info[key] = None
                    if key in managed_object:
                        info[key] = managed_object[key]

                info['member'] = []
                if 'TABLE_member' in managed_object:
                    if 'ROW_member' in managed_object['TABLE_member']:
                        if isinstance(managed_object['TABLE_member']['ROW_member'], dict):
                            item = {}
                            item['port'] = managed_object['TABLE_member']['ROW_member']['port']
                            item['status'] = managed_object['TABLE_member']['ROW_member']['port-status']
                            info['member'].append(
                                item
                            )
                        if isinstance(managed_object['TABLE_member']['ROW_member'], list):
                            for item_mo in managed_object['TABLE_member']['ROW_member']:
                                item = {}
                                item['port'] = item_mo['port']
                                item['status'] = item_mo['port-status']
                                info['member'].append(
                                    item
                                )

                self.pc_state.append(
                    info
                )

        return self.pc_state

    def get_pc_state(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.pc_state is not None:
                return self.pc_state

        pc_state_mo = self.get_pc_state_mo(cache_enabled=cache_enabled)
        if pc_state_mo is None:
            self.log.error(
                'get_pc_state',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_pc_state_info(pc_state_mo)
