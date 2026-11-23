class PcTrafficInfo():
    def __init__(self):
        self.pc_traffic = None

    def get_pc_traffic_info(self, pc_traffic_mo):
        if pc_traffic_mo is None:
            return None

        self.pc_traffic = []
        if len(pc_traffic_mo) > 0:
            for managed_object in pc_traffic_mo['TABLE_channel']['ROW_channel']:
                info = {}
                info['__Output'] = {}
                info['nexus_name'] = self.nexus_name

                keys = [
                    'chanId',
                    'port',
                    'rx-ucst',
                    'tx-ucst',
                    'rx-mcst',
                    'tx-mcst',
                    'rx-bcst',
                    'tx-bcst'
                ]
                for key in keys:
                    info[key] = None
                    if key in managed_object:
                        info[key] = managed_object[key]

                self.pc_traffic.append(
                    info
                )

        return self.pc_traffic

    def get_pc_traffic(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.pc_traffic is not None:
                return self.pc_traffic

        pc_traffic_mo = self.get_pc_traffic_mo(cache_enabled=cache_enabled)
        if pc_traffic_mo is None:
            self.log.error(
                'get_pc_traffic',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        return self.get_pc_traffic_info(pc_traffic_mo)
