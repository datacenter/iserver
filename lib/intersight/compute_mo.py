class ComputeMo():
    def __init__(self):
        pass

    def get_management_ip(self, server_mo):
        if 'KvmIpAddresses' in server_mo:
            for kvm_ip in server_mo['KvmIpAddresses']:
                if kvm_ip['ClassId'] == 'compute.IpAddress':
                    return kvm_ip['Address']
        return None

    def get(self, server_id, settings={}):
        server_mo = self.rack_handler.get(server_id)
        if server_mo is None:
            server_mo = self.blade_handler.get(server_id)

        if server_mo is None:
            return None

        return self.get_server_info(server_mo, settings, log_id=self.log_id)

    def get_mo(self, match_rules=None, include_rack=False, rack_expand=None, include_blade=False, blade_expand=None, cache_ttl=None):
        servers_mo = []

        if include_rack:
            rack_servers = None
            if rack_expand is None and cache_ttl is not None:
                rack_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if rack_servers is None:
                if rack_expand is not None and len(rack_expand) > 0:
                    self.rack_handler.set_get_expand(','.join(rack_expand))
                rack_servers = self.rack_handler.get_all()
                self.cache_handler.set_intersight_cache_entry(
                    'inventory.rack.%s' % (self.iaccount),
                    rack_servers
                )

            if rack_servers is not None:
                servers_mo = servers_mo + rack_servers

        if include_blade:
            blade_servers = None
            if blade_expand is None and cache_ttl is not None:
                blade_servers = self.cache_handler.get_intersight_cache_entry(
                    'inventory.blade.%s' % (self.iaccount),
                    cache_ttl=cache_ttl
                )

            if blade_servers is None:
                if blade_expand is not None and len(blade_expand) > 0:
                    self.blade_handler.set_get_expand(','.join(blade_expand))
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
