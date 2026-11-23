import time
import json
import traceback


class OspSecurityGroupApi():
    def __init__(self):
        self.security_group_mo = None

    def get_security_group_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.security_group_mo is not None:
                return self.security_group_mo

        api_handler = self.get_api_neutron(cache_enabled=cache_enabled)
        if api_handler is None:
            self.log.error(
                'get_security_group_mo',
                'No api handler'
            )
            return None

        try:
            start_time = int(time.time() * 1000)
            self.security_group_mo = api_handler.list_security_groups()['security_groups']
            self.log.osp(
                'get',
                'security_groups',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('osp.get_security_group_mo', traceback.format_exc())
            self.log.osp(
                'get',
                'security_groups',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.security_group_mo

    def create_security_group_rule_mo(
            self,
            security_group_id,
            ethertype,
            protocol,
            direction,
            port_range_min = None,
            port_range_max = None,
            remote_ip_prefix = '0.0.0.0/0',
            description = None
        ):
        try:
            api_handler = self.get_api_neutron(cache_enabled=False)
            if api_handler is None:
                self.log.error(
                    'create_security_group_rule_mo',
                    'No api handler'
                )
                return None

            # https://docs.openstack.org/tempest/latest/_modules/network/test_security_groups.html
            body = {}
            body['security_group_rule'] = {}
            body['security_group_rule']['security_group_id'] = security_group_id
            body['security_group_rule']['ethertype'] = ethertype
            body['security_group_rule']['protocol'] = protocol
            body['security_group_rule']['direction'] = direction
            body['security_group_rule']['remote_ip_prefix'] = remote_ip_prefix
            if description is not None:
                body['security_group_rule']['description'] = description
            if port_range_min is not None:
                body['security_group_rule']['port_range_min'] = port_range_min
            if port_range_max is not None:
                body['security_group_rule']['port_range_max'] = port_range_max

            self.log.debug(
                'create_security_group_rule_mo',
                'Create security group rule: %s' % (json.dumps(body, indent=4))
            )
            ret = api_handler.create_security_group_rule(body=body)
            rule_id = ret['security_group_rule']['id']

        except BaseException:
            self.log.error(
                'create_security_group_rule_mo',
                'Neutron API exception'
            )
            self.log.error(
                'create_security_group_rule_mo',
                traceback.format_exc()
            )
            return None

        return rule_id

    def delete_security_group_rule_mo(self, security_group_rule_id):
        try:
            api_handler = self.get_api_neutron(cache_enabled=False)
            if api_handler is None:
                self.log.error(
                    'delete_security_group_rule_mo',
                    'No api handler'
                )
                return False

            api_handler.delete_security_group_rule(security_group_rule_id)

        except BaseException:
            self.log.error(
                'delete_security_group_rule_mo',
                'Neutron API exception'
            )
            self.log.error(
                'delete_security_group_rule_mo',
                traceback.format_exc()
            )
            return False

        return True
