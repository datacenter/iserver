class ComputeMo():
    def __init__(self):
        pass

    def get_management_ip(self, server_mo):
        if 'KvmIpAddresses' in server_mo:
            for kvm_ip in server_mo['KvmIpAddresses']:
                if kvm_ip['ClassId'] == 'compute.IpAddress':
                    return kvm_ip['Address']
        return None

    def get_mo(self, match_rules=None, include_rack=False, include_blade=False, cache_ttl=None):
        servers_mo = []

        if include_rack:
            rack_servers = None
            if cache_ttl is not None:
                rack_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if rack_servers is None:
                rack_servers = self.rack_handler.get_all()
                self.cache_handler.set_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    rack_servers
                )

            if rack_servers is not None:
                servers_mo = servers_mo + rack_servers

        if include_blade:
            blade_servers = None
            if cache_ttl is not None:
                blade_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.blade.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if blade_servers is None:
                blade_servers = self.blade_handler.get_all()
                self.cache_handler.set_intersight_cache_entry(
                    'inventory.blade.%s' % (self.iaccount),
                    blade_servers
                )

            if blade_servers is not None:
                servers_mo = servers_mo + blade_servers

        selected_servers_mo = []
        for server_mo in servers_mo:
            server_mo['ManagementIp'] = self.get_management_ip(server_mo)
            if self.match_server_mo(server_mo, match_rules):
                selected_servers_mo.append(server_mo)

        return selected_servers_mo
