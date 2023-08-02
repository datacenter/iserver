from lib import filter_helper


class PolicyGroupAccessInterfaceVpcInfo():
    def __init__(self):
        self.policy_group_access_interface_vpc = None

    def get_policy_group_access_interface_vpc_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "descr": "ACI2 vEPC CL2201-2202 to ESX20 Policy Group  (Created by Ansible)",
        # "dn": "uni/infra/funcprof/accbundle-ESX20-CDC-22_PolGrp",
        # "extMngdBy": "",
        # "lagT": "node",
        # "lcOwn": "local",
        # "modTs": "2022-07-08T15:21:38.449+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "ESX20-CDC-22_PolGrp",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "status": "",
        # "uid": "15374",
        # "userdom": ":all:common:",
        info = {}
        info['__Output'] = {}

        keys = [
            'annotation',
            'descr',
            'dn',
            'lagT',
            'name'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        for policy_name in self.policy_group_access_interface_vpc_policies:
            info[policy_name] = self.get_policy_interface_reference_attributes(
                managed_object[policy_name]
            )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_policy_groups_access_interface_vpc_info(self):
        if self.policy_group_access_interface_vpc is not None:
            return self.policy_group_access_interface_vpc

        managed_objects = self.get_policy_group_access_interface_vpc_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_vpc = []

        for managed_object in managed_objects:
            policy_group_info = self.get_policy_group_access_interface_vpc_info(
                managed_object
            )
            self.policy_group_access_interface_vpc.append(
                policy_group_info
            )

        self.policy_group_access_interface_vpc = sorted(
            self.policy_group_access_interface_vpc,
            key=lambda i: i['name'].lower()
        )

        self.log.apic_mo(
            'infraAccBndlGrp.info',
            self.policy_group_access_interface_vpc
        )

        return self.policy_group_access_interface_vpc

    def match_policy_group_access_interface_vpc(self, policy_group_info, policy_group_filter):
        if policy_group_filter is None or len(policy_group_filter) == 0:
            return True

        for ap_rule in policy_group_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_group_info['name']):
                    return False

            if key == 'aaep':
                if not filter_helper.match_string(value, policy_group_info['infraRsAttEntP']['name']):
                    return False

            if key == 'policy':
                found = False
                for policy_name in self.policy_group_access_interface_vpc_policies:
                    if filter_helper.match_string(value, policy_group_info[policy_name]['name']):
                        found = True
                        break

                if not found:
                    return False

            if key == 'fault':
                if value == 'any':
                    if not policy_group_info['isAnyFault']:
                        return False

                if value not in ['any']:
                    self.log.error(
                        'match_policy_group_access_interface_vpc',
                        'Unsupported fault filtering value: %s' % (value)
                    )

            if key not in ['name', 'aaep', 'fault', 'policy']:
                found = False
                for policy_name in self.policy_group_access_interface_vpc_policies:
                    if key == policy_name:
                        if filter_helper.match_string(value, policy_group_info[policy_name]['name']):
                            found = True
                            break

                if not found:
                    return False

            # if key == 'policy':
            #     if len(value.split(':')) > 2:
            #         self.log.error(
            #             'match_policy_group_access_interface_vpc',
            #             'Unsupported policy filter rule: %s' % (ap_rule)
            #         )
            #         return False

            #     if len(value.split(':')) == 1:
            #         found = False
            #         for policy in policy_group_info['policies']:
            #             if policy['name'] is not None:
            #                 if filter_helper.match_string(value, policy['name']):
            #                     found = True
            #                     break

            #         if not found:
            #             return False

            #     if len(value.split(':')) == 2:
            #         found = False
            #         for policy in policy_group_info['policies']:
            #             if policy['name'] is not None:
            #                 if filter_helper.match_string(value.split(':', maxsplit=1)[0], policy['type']):
            #                     if filter_helper.match_string(value.split(':')[1], policy['name']):
            #                         found = True
            #                         break

            #         if not found:
            #             return False

        return True

    def get_policy_groups_access_interface_vpc(
            self,
            policy_group_filter=None,
            aaep_info=False,
            node_info=False,
            vlan_info=False,
            fault_info=False,
            hfault_info=False,
            event_info=False,
            audit_info=False,
            hfault_filter=None,
            event_filter=None,
            audit_filter=None
            ):
        all_policy_groups = self.get_policy_groups_access_interface_vpc_info()
        if all_policy_groups is None:
            return None

        policy_groups = []

        for policy_group_info in all_policy_groups:
            if not self.match_policy_group_access_interface_vpc(policy_group_info, policy_group_filter):
                continue

            if aaep_info:
                policy_group_info['aaep'] = None
                aaep = self.get_policy_global_aae(
                    policy_global_aae_filter=['name:%s' % (policy_group_info['infraRsAttEntP']['name'])],
                    domain_info=True
                )
                if aaep is not None:
                    if len(aaep) == 1:
                        policy_group_info['aaep'] = aaep[0]

            if node_info:
                policy_group_node_info = self.get_policy_group_access_interface_vpc_node(
                    policy_group_info['name']
                )
                policy_group_info['node'] = None
                policy_group_info['interface'] = None
                if policy_group_node_info is not None:
                    policy_group_info['node'] = policy_group_node_info['node']
                    policy_group_info['interface'] = policy_group_node_info['interface']

            # if node_info:
            #     policy_group_info['nodes'] = []

            #     vpc_nodes = self.get_policy_group_access_interface_vpc_nodes(
            #         policy_group_filter=['name:%s' % (policy_group_info['name'])],
            #         port_info=port_info
            #     )
            #     if vpc_nodes is not None:
            #         if len(vpc_nodes) == 1:
            #             policy_group_info['nodes'] = vpc_nodes[0]['nodes']
            #             if port_info:
            #                 policy_group_info['ports'] = vpc_nodes[0]['ports']

            if vlan_info:
                if policy_group_info['interface'] is not None:
                    for interface in policy_group_info['interface']:
                        interface['vlan'] = []
                        interface['operSt'] = '--'
                        interface['operMode'] = '--'

                        if interface['intf_type'] == 'l1PhysIf':
                            interface_info = self.get_interface_phy(
                                interface['pod_id'],
                                interface['node_id'],
                                interface['intf_name'],
                                epg_stats_info=True
                            )
                            if interface_info is not None:
                                interface['operSt'] = interface_info['stats']['operSt']
                                interface['operMode'] = interface_info['stats']['operMode']
                                for intf_epg_stats in interface_info['epg_stats']:
                                    if intf_epg_stats['vlan'] is not None:
                                        if intf_epg_stats['vlan']['evlan'] not in interface['vlan']:
                                            interface['vlan'].append(
                                                intf_epg_stats['vlan']['evlan']
                                            )

                                interface['vlan'] = sorted(
                                    interface['vlan']
                                )
                                interface['vlans'] = ','.join(
                                    interface['vlan']
                                )

            if fault_info:
                policy_group_info['faultInst'] = self.get_policy_group_access_interface_vpc_id_fault(
                    policy_group_info['name'],
                    'faultInst'
                )

            if hfault_info:
                policy_group_info['faultRecord'] = self.get_policy_group_access_interface_vpc_id_fault(
                    policy_group_info['name'],
                    'faultRecord',
                    fault_filter=hfault_filter
                )

            if event_info:
                policy_group_info['eventLog'] = self.get_policy_group_access_interface_vpc_id_event(
                    policy_group_info['name'],
                    event_filter=event_filter
                )

            if audit_info:
                policy_group_info['auditLog'] = self.get_policy_group_access_interface_vpc_id_audit(
                    policy_group_info['name'],
                    audit_filter=audit_filter
                )

            policy_groups.append(
                policy_group_info
            )

        policy_groups = sorted(
            policy_groups,
            key=lambda i: i['name'].lower()
        )

        return policy_groups

    def get_policy_group_access_interface_vpc(self, name):
        policy_group_info = self.get_policy_groups_access_interface_vpc(
            policy_group_filter=['name:%s' % (name)]
        )

        if policy_group_info is None:
            return None

        if len(policy_group_info) == 0:
            return None

        if len(policy_group_info) > 1:
            self.log.error(
                'get_policy_group_access_interface_vpc',
                'Unexpected policy group count'
            )
            return None

        return policy_group_info[0]
