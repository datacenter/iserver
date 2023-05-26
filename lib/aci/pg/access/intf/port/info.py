from lib import filter_helper


class PolicyGroupAccessInterfacePortInfo():
    def __init__(self):
        self.policy_group_access_interface_port = None

    def get_policy_group_access_interface_port_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'annotation',
            'descr',
            'dn',
            'name',
            'aaep_name',
            'policy'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_policy_groups_access_interface_port_info(self):
        if self.policy_group_access_interface_port is not None:
            return self.policy_group_access_interface_port

        managed_objects = self.get_policy_group_access_interface_port_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_port = []

        for managed_object in managed_objects:
            policy_group_info = self.get_policy_group_access_interface_port_info(
                managed_object
            )
            self.policy_group_access_interface_port.append(
                policy_group_info
            )

        self.policy_group_access_interface_port = sorted(
            self.policy_group_access_interface_port,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'infraAccPortGrp.info',
            self.policy_group_access_interface_port
        )

        return self.policy_group_access_interface_port

    def match_policy_group_access_interface_port(self, policy_group_info, policy_group_filter):
        if policy_group_filter is None or len(policy_group_filter) == 0:
            return True

        for ap_rule in policy_group_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_group_info['name']):
                    return False

            if key == 'aaep':
                if not filter_helper.match_string(value, policy_group_info['aaep_name']):
                    return False

            if key == 'policy':
                found = False
                for policy_name in policy_group_info['policy']:
                    if filter_helper.match_string(value, policy_group_info['policy'][policy_name]):
                        found = True
                        break

                if not found:
                    return False

            if key not in ['name', 'aaep', 'policy']:
                found = False
                for policy_name in policy_group_info['policy']:
                    if key == policy_name:
                        if filter_helper.match_string(value, policy_group_info['policy'][policy_name]):
                            found = True
                            break

                if not found:
                    return False

        return True

    def get_policy_groups_access_interface_port(self, policy_group_filter=None, aaep_info=False):
        all_policy_groups = self.get_policy_groups_access_interface_port_info()
        if all_policy_groups is None:
            return None

        policy_groups = []

        for policy_group_info in all_policy_groups:
            if not self.match_policy_group_access_interface_port(policy_group_info, policy_group_filter):
                continue

            if aaep_info:
                policy_group_info['aaep'] = None
                aaep = self.get_policy_global_aae(
                    policy_global_aae_filter=['name:%s' % (policy_group_info['aaep_name'])]
                )
                if aaep is not None:
                    if len(aaep) == 1:
                        policy_group_info['aaep'] = aaep[0]

            policy_groups.append(
                policy_group_info
            )

        policy_groups = sorted(
            policy_groups,
            key=lambda i: i['name'].lower()
        )

        return policy_groups

    def get_policy_group_access_interface_port(self, name):
        policy_group_info = self.get_policy_groups_access_interface_port(
            policy_group_filter=['name:%s' % (name)]
        )

        if policy_group_info is None:
            return None

        if len(policy_group_info) == 0:
            return None

        if len(policy_group_info) > 1:
            self.log.error(
                'get_policy_group_access_interface_port',
                'Unexpected policy group count'
            )
            return None

        return policy_group_info[0]
