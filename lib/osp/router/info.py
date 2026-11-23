from lib import filter_helper


class OspRouterInfo():
    def __init__(self):
        self.router = None

    def get_router_info(self, router_mo):
        if router_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'tenant_id',
            'admin_state_up',
            'status',
            'availability_zones',
            'ha',
            'routes',
            'created_at',
            'updated_at'
        ]
        for key in keys:
            info[key] = None
            if key in router_mo:
                info[key] = router_mo[key]

        info['network_id'] = router_mo['external_gateway_info']['network_id']
        info['fixed_ips'] = router_mo['external_gateway_info']['external_fixed_ips']
        info['snat'] = router_mo['external_gateway_info']['enable_snat']

        if info['status'] == 'ACTIVE':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        if info['admin_state_up']:
            info['adminTick'] = '\u2713'
            info['__Output']['adminTick'] = 'Green'
        else:
            info['adminTick'] = '\u2717'
            info['__Output']['adminTick'] = 'Green'

        if info['ha']:
            info['haTick'] = '\u2713'
        else:
            info['haTick'] = '\u2717'

        if info['snat']:
            info['snatTick'] = '\u2713'
        else:
            info['snatTick'] = '\u2717'

        info['created_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['updated_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_routers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.router is not None:
                return self.router

        managed_objects = self.get_router_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.log.osp_mo(
            'routers',
            managed_objects
        )

        self.router = []
        for managed_object in managed_objects:
            router_info = self.get_router_info(
                managed_object
            )
            self.router.append(
                router_info
            )

        self.log.osp_mo(
            'routers.info',
            self.router
        )

        return self.router

    def match_router(self, router_info, router_filter):
        if router_filter is None or len(router_filter) == 0:
            return True

        for ap_rule in router_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, router_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, router_info['name']):
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, router_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in router_info:
                    if not filter_helper.match_string(value, router_info['tenant_name']):
                        return False

            if key == 'network_id':
                key_found = True
                if not filter_helper.match_string(value, router_info['network_id']):
                    return False

            if key == 'network_name':
                key_found = True
                if 'network_name' in router_info:
                    if not filter_helper.match_string(value, router_info['network_name']):
                        return False

            if not key_found:
                self.log.error(
                    'match_router',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_routers(self, object_filter=None, tenant_info=False, network_info=False, subnet_info=False, port_info=False, cache_enabled=True):
        all_routers = self.get_routers_info(cache_enabled=cache_enabled)
        if all_routers is None:
            return None

        routers = []

        for router_info in all_routers:
            if not self.match_router(router_info, object_filter):
                continue

            if tenant_info:
                router_info['tenant_name'] = self.get_tenant_name(
                    router_info['tenant_id'],
                    cache_enabled=cache_enabled
                )

                if not self.match_router(router_info, object_filter):
                    continue

            if network_info:
                router_info['network_name'] = self.get_network_name(
                    router_info['network_id'],
                    cache_enabled=cache_enabled
                )

                if not self.match_router(router_info, object_filter):
                    continue

            if subnet_info:
                for fixed_ip in router_info['fixed_ips']:
                    router_subnet_info = self.get_subnet(
                        fixed_ip['subnet_id']
                    )
                    if router_subnet_info is None:
                        self.log.error(
                            'get_routers',
                            'Failed to find subnet: %s' % (fixed_ip['subnet_id'])
                        )
                    else:
                        fixed_ip['subnet_name'] = router_subnet_info['name']
                        fixed_ip['gateway_ip'] = router_subnet_info['gateway_ip']
                        fixed_ip['cidr'] = router_subnet_info['cidr']

                if not self.match_router(router_info, object_filter):
                    continue

            if port_info:
                router_info['port_info'] = []
                for fixed_ip in router_info['fixed_ips']:
                    router_port_filter = []
                    router_port_filter.append(
                        'subnet_id:%s' % (fixed_ip['subnet_id'])
                    )
                    router_port_info = self.get_ports(
                        object_filter=router_port_filter,
                        vm_info=True
                    )
                    if router_port_info is None:
                        self.log.error(
                            'get_routers',
                            'Failed to get subnet ports: %s' % (fixed_ip['subnet_id'])
                        )
                    else:
                        for rpi in router_port_info:
                            if rpi['type'] == 'Floating' and rpi['vm_tenant_name'] is None:
                                port_details = self.get_floating_ip_port(
                                    floating_ip=rpi['ips']
                                )
                                if port_details is not None:
                                    rpi['vm_tenant_name'] = port_details['vm_name']

                        router_info['port_info'] = router_info['port_info'] + router_port_info

                if not self.match_router(router_info, object_filter):
                    continue

            routers.append(
                router_info
            )

        routers = sorted(
            routers,
            key=lambda i: i['name'].lower()
        )

        return routers

    def get_router(self, router_id=None, router_name=None, tenant_info=False, network_info=False, port_info=False, cache_enabled=True):
        object_filter = []
        if router_id is not None:
            object_filter.append(
                'id:%s' % (router_id)
            )
        if router_name is not None:
            object_filter.append(
                'name:%s' % (router_name)
            )

        routers = self.get_routers(
            object_filter=object_filter,
            tenant_info=tenant_info,
            network_info=network_info,
            port_info=port_info,
            cache_enabled=cache_enabled
        )
        if routers is None or len(routers) != 1:
            return None

        return routers[0]

    def get_router_name(self, router_id, cache_enabled=True):
        router_info = self.get_router(
            router_id=router_id,
            cache_enabled=cache_enabled
        )
        if router_info is None:
            return None
        return router_info['name']
