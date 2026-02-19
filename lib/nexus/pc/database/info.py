class PcDatabaseInfo():
    def __init__(self):
        self.pc_database = None

    def get_pc_database_info(self, pc_database_mo):
        if pc_database_mo is None:
            return None

        self.pc_database = []
        for managed_object in pc_database_mo['TABLE_interface']['ROW_interface']:
            info = {}
            info['__Output'] = {}
            info['nexus_name'] = self.nexus_name

            keys = [
                'interface',
                'last-membership-update',
                'total-ports',
                'total-up-ports',
                'first_operational-port',
                'age-of-channel',
                'time-since-last-bundle',
                'last-bundled-member'
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
                        item['mode'] = managed_object['TABLE_member']['ROW_member']['mode']
                        item['status'] = managed_object['TABLE_member']['ROW_member']['port-status']
                        info['member'].append(
                            item
                        )
                    if isinstance(managed_object['TABLE_member']['ROW_member'], list):
                        for item_mo in managed_object['TABLE_member']['ROW_member']:
                            item = {}
                            item['port'] = item_mo['port']
                            item['mode'] = item_mo['mode']
                            item['status'] = item_mo['port-status']
                            info['member'].append(
                                item
                            )

            self.pc_database.append(
                info
            )

        return self.pc_database

    def get_pc_database(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.pc_database is not None:
                return self.pc_database

        pc_database_mo = self.get_pc_database_mo(cache_enabled=cache_enabled)
        if pc_database_mo is None:
            self.log.error(
                'get_pc_database',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_pc_database_info(pc_database_mo)
