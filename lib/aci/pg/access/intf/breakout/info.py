from lib import filter_helper


class PolicyGroupAccessInterfaceBreakoutInfo():
    def __init__(self):
        self.policy_group_access_interface_breakout = None

    def get_policy_group_access_interface_breakout_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'annotation',
            'brkoutMap',
            'dn',
            'name'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_policy_groups_access_interface_breakout_info(self):
        if self.policy_group_access_interface_breakout is not None:
            return self.policy_group_access_interface_breakout

        managed_objects = self.get_policy_group_access_interface_breakout_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_breakout = []

        for managed_object in managed_objects:
            policy_group_info = self.get_policy_group_access_interface_breakout_info(
                managed_object
            )
            self.policy_group_access_interface_breakout.append(
                policy_group_info
            )

        self.policy_group_access_interface_breakout = sorted(
            self.policy_group_access_interface_breakout,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'infraBrkoutPortGrp.info',
            self.policy_group_access_interface_breakout
        )

        return self.policy_group_access_interface_breakout

    def match_policy_group_access_interface_breakout(self, policy_group_info, policy_group_filter):
        if policy_group_filter is None or len(policy_group_filter) == 0:
            return True

        for ap_rule in policy_group_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_group_info['name']):
                    return False

        return True

    def get_policy_groups_access_interface_breakout(self, policy_group_filter=None):
        all_policy_groups = self.get_policy_groups_access_interface_breakout_info()
        if all_policy_groups is None:
            return None

        policy_groups = []

        for policy_group_info in all_policy_groups:
            if not self.match_policy_group_access_interface_breakout(policy_group_info, policy_group_filter):
                continue

            policy_groups.append(
                policy_group_info
            )

        policy_groups = sorted(
            policy_groups,
            key=lambda i: i['name'].lower()
        )

        return policy_groups

    def get_policy_group_access_interface_breakout(self, name):
        policy_group_info = self.get_policy_groups_access_interface_breakout(
            policy_group_filter=['name:%s' % (name)]
        )

        if policy_group_info is None:
            return None

        if len(policy_group_info) == 0:
            return None

        if len(policy_group_info) > 1:
            self.log.error(
                'get_policy_group_access_interface_breakout',
                'Unexpected policy group count'
            )
            return None

        return policy_group_info[0]
