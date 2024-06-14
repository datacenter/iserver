from lib import filter_helper


class OspSecurityGroupInfo():
    def __init__(self):
        self.security_group = None

    def get_security_group_info(self, security_group_mo):
        if security_group_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'id',
            'name',
            'tenant_id',
            'description',
            'created_at',
            'updated_at'
        ]

        for key in keys:
            info[key] = None
            if key in security_group_mo:
                info[key] = security_group_mo[key]

        info['rule'] = []
        for rule_mo in security_group_mo['security_group_rules']:
            rule_info = {}
            rule_info['__Output'] = {}

            keys = [
                'id',
                'ethertype',
                'direction',
                'protocol',
                'port_range_min',
                'port_range_max',
                'remote_ip_prefix',
                'remote_group_id',
                'created_at',
                'updated_at'
            ]
            for key in keys:
                rule_info[key] = None
                if key in rule_mo:
                    rule_info[key] = rule_mo[key]

            rule_info['port_range'] = None
            if rule_info['port_range_min'] is not None and rule_info['port_range_max'] is not None:
                rule_info['port_range'] = '%s-%s' % (
                    rule_info['port_range_min'],
                    rule_info['port_range_max']
                )

            rule_info['create_age'] = self.convert_timestamp_to_age(
                rule_info['created_at'],
                on_error='--'
            )

            rule_info['update_age'] = self.convert_timestamp_to_age(
                rule_info['updated_at'],
                on_error='--'
            )

            info['rule'].append(
                rule_info
            )

        info['rule'] = sorted(
            info['rule'],
            key=lambda i:(
                i['ethertype'],
                i['direction']
            )
        )

        info['rule_count'] = len(
            info['rule']
        )

        info['create_age'] = self.convert_timestamp_to_age(
            info['created_at'],
            on_error='--'
        )

        info['update_age'] = self.convert_timestamp_to_age(
            info['updated_at'],
            on_error='--'
        )

        return info

    def get_security_groups_info(self, cache_enabled=True):
        if cache_enabled:
            if self.security_group is not None:
                return self.security_group

        managed_objects = self.get_security_group_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.security_group = []
        for managed_object in managed_objects:
            security_group_info = self.get_security_group_info(
                managed_object
            )
            self.security_group.append(
                security_group_info
            )

        self.log.osp_mo(
            'security_groups',
            self.security_group
        )

        return self.security_group

    def match_security_group(self, security_group_info, security_group_filter):
        if security_group_filter is None or len(security_group_filter) == 0:
            return True

        for ap_rule in security_group_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'id':
                key_found = True
                if not filter_helper.match_string(value, security_group_info['id']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, security_group_info['name']):
                    return False

            if key == 'names':
                key_found = True
                found = False
                for item in value.split(','):
                    (tenant_name, name) = item.split('/')
                    if 'tenant_name' in security_group_info and 'name' in security_group_info:
                        if filter_helper.match_string(tenant_name, security_group_info['tenant_name']):
                            if filter_helper.match_string(name, security_group_info['name']):
                                found = True
                                break

                if not found:
                    return False

            if key == 'tenant_id':
                key_found = True
                if not filter_helper.match_string(value, security_group_info['tenant_id']):
                    return False

            if key == 'tenant_name':
                key_found = True
                if 'tenant_name' in security_group_info:
                    if not filter_helper.match_string(value, security_group_info['tenant_name']):
                        return False

            if key == 'vm_name':
                key_found = True
                if 'port' in security_group_info:
                    found = False
                    for port_info in security_group_info['port']:
                        if filter_helper.match_string(value, port_info['vm_tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if key == 'mac':
                key_found = True
                if 'port' in security_group_info:
                    found = False
                    for port_info in security_group_info['port']:
                        if filter_helper.match_mac(value, port_info['mac_address']):
                            found = True
                            break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_security_group',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_security_groups(self, object_filter=None, tenant_info=False, rule_info=False, port_info=False, cache_enabled=True):
        all_security_groups = self.get_security_groups_info(cache_enabled=cache_enabled)
        if all_security_groups is None:
            return None

        security_groups = []

        for security_group_info in all_security_groups:
            if not self.match_security_group(security_group_info, object_filter):
                continue

            if tenant_info:
                security_group_info['tenant_name'] = ''
                if len(security_group_info['tenant_id']) > 0:
                    security_group_info['tenant_name'] = self.get_tenant_name(
                        security_group_info['tenant_id']
                    )

                if not self.match_security_group(security_group_info, object_filter):
                    continue

            if rule_info:
                for rule in security_group_info['rule']:
                    rule['remote_group_name'] = None
                    if rule['remote_group_id'] is not None:
                        for sg_info in all_security_groups:
                            if sg_info['id'] == rule['remote_group_id']:
                                remote_group_tenant = self.get_tenant_name(
                                    sg_info['tenant_id']
                                )
                                if remote_group_tenant is None:
                                    remote_group_tenant = '--'

                                rule['remote_group_name'] = '%s/%s' % (
                                    remote_group_tenant,
                                    sg_info['name']
                                )

                if not self.match_security_group(security_group_info, object_filter):
                    continue

            if port_info:
                port_object_filter = []
                if len(security_group_info['tenant_name']) == 0:
                    port_object_filter.append(
                        'sg:%s' % (security_group_info['name'])
                    )
                else:
                    port_object_filter.append(
                        'sg:%s/%s' % (
                            security_group_info['tenant_name'],
                            security_group_info['name']
                        )
                    )

                security_group_info['port'] = self.get_ports(
                    object_filter=port_object_filter,
                    security_info=True,
                    vm_info=True
                )

                if not self.match_security_group(security_group_info, object_filter):
                    continue

            security_groups.append(
                security_group_info
            )

        if tenant_info:
            security_groups = sorted(
                security_groups,
                key=lambda i: (
                    i['tenant_name'],
                    i['name']
                )
            )
        else:
            security_groups = sorted(
                security_groups,
                key=lambda i: i['name']
            )

        return security_groups

    def get_security_group_tenant_name(self, security_group_id, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'id:%s' % (security_group_id)
        )
        security_groups_info = self.get_security_groups(
            object_filter=object_filter,
            tenant_info=True,
            cache_enabled=cache_enabled
        )
        if security_groups_info is None or len(security_groups_info) != 1:
            return None

        tenant_name = security_groups_info[0]['tenant_name']
        if tenant_name is None or len(tenant_name) == 0:
            return '--/%s' % (security_groups_info[0]['name'])

        return '%s/%s' % (tenant_name, security_groups_info[0]['name'])

    def get_security_group(self, security_group_id=None, security_group_name=None, tenant_id=None, tenant_name=None, tenant_info=False, rule_info=False, port_info=False, cache_enabled=True):
        if security_group_id is None and security_group_name is None:
            self.log.error(
                'get_security_group',
                'security group id or name expected'
            )
            return None

        if security_group_name is not None:
            if tenant_id is None and tenant_name is None:
                self.log.error(
                    'get_security_group',
                    'tenant id or name expected'
                )
                return None

        object_filter = []
        if security_group_id is not None:
            object_filter.append(
                'id:%s' % (security_group_id)
            )

        if security_group_name is not None:
            object_filter.append(
                'name:%s' % (security_group_name)
            )

        if tenant_id is not None:
            object_filter.append(
                'tenant_id:%s' % (tenant_id)
            )

        if tenant_name is not None:
            object_filter.append(
                'tenant_name:%s' % (tenant_name)
            )

        security_groups = self.get_security_groups(
            object_filter=object_filter,
            tenant_info=tenant_info,
            rule_info=rule_info,
            port_info=port_info,
            cache_enabled=cache_enabled
        )
        if security_groups is None or len(security_groups) != 1:
            return None

        return security_groups[0]

    def get_security_group_rule(self, security_group_rule_id, security_group_id = None):
        if security_group_id is None:
            security_groups = self.get_security_groups(
                rule_info=True
            )
        else:
            security_group_info = self.get_security_group(
                security_group_id=security_group_id
            )
            if security_group_info is None:
                return None
            security_groups = [security_group_info]

        for security_group in security_groups:
            for rule in security_group['rule']:
                if rule['id'] == security_group_rule_id:
                    return rule

        return None

    def is_security_group_rule(self, security_group_rule_id, security_group_id = None):
        if self.get_security_group_rule(security_group_rule_id, security_group_id=security_group_id) is None:
            return False
        return True
