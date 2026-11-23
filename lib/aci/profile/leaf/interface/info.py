from lib import filter_helper


class ProfileLeafInterfaceInfo():
    def __init__(self):
        self.profile_leaf_interface = None

    def get_profile_leaf_interface_node_ids(self, profile_name):
        node_ids = []

        managed_objects = self.get_profile_leaf_interface_node_mo(
            profile_name
        )
        if managed_objects is None:
            return node_ids

        for managed_object in managed_objects:
            for deploy_mo in managed_object['pconsNodeDeployCtx']:
                if deploy_mo['nodeId'] not in node_ids:
                    node_ids.append(
                        deploy_mo['nodeId']
                    )

        return node_ids

    def get_profile_leaf_interface_node_interfaces_info(self, profile_name, node_id):
        info = []

        managed_objects = self.get_profile_leaf_interface_node_interface_mo(
            profile_name,
            node_id
        )
        if managed_objects is None:
            return info

        for managed_object in managed_objects:
            item = {}
            for key in ['ctxClass', 'ctxDn']:
                item[key] = managed_object[key]

            item['podId'] = 'unknown'
            item['nodeId'] = 'unknown'
            item['interfaceId'] = '-1/-1'

            if item['ctxClass'] == 'l1PhysIf':
                item['podId'] = item['ctxDn'].split('/')[1].split('-')[1]
                item['nodeId'] = item['ctxDn'].split('/')[2].split('-')[1]
                item['interfaceId'] = item['ctxDn'].split('phys-')[1].split('[')[1].split(']')[0]

            info.append(
                item
            )

        info = sorted(
            info,
            key=lambda i: (
                i['podId'],
                i['nodeId'],
                int(i['interfaceId'].split('/')[-1])
            )
        )

        return info

    def get_profile_leaf_interface_reln_info(self, profile_name):
        reln_info = []
        managed_objects = self.get_profile_leaf_interface_reln_mo(
            profile_name
        )
        if managed_objects is None:
            return reln_info

        for managed_object in managed_objects:
            reln_info.append(
                managed_object
            )

        return reln_info

    def get_profile_leaf_interface_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in ['dn', 'name']:
            info[key] = managed_object[key]

        info['selector'] = []
        for port_mo in managed_object['infraHPortS']:
            port_info = {}
            port_info['name'] = port_mo['name']
            if 'infraPortBlk' in port_mo:
                port_info['from'] = '%s/%s' % (
                    port_mo['infraPortBlk']['fromCard'],
                    port_mo['infraPortBlk']['fromPort']
                )
                port_info['to'] = '%s/%s' % (
                    port_mo['infraPortBlk']['toCard'],
                    port_mo['infraPortBlk']['toPort']
                )
                if port_info['from'] == port_info['to']:
                    port_info['block'] = port_info['from']
                else:
                    port_info['block'] = '%s-%s' % (
                        port_info['from'],
                        port_info['to']
                    )

            if 'infraSubPortBlk' in port_mo:
                port_info['from'] = '%s/%s/%s' % (
                    port_mo['infraSubPortBlk']['fromCard'],
                    port_mo['infraSubPortBlk']['fromPort'],
                    port_mo['infraSubPortBlk']['fromSubPort']
                )
                port_info['to'] = '%s/%s/%s' % (
                    port_mo['infraSubPortBlk']['toCard'],
                    port_mo['infraSubPortBlk']['toPort'],
                    port_mo['infraSubPortBlk']['toSubPort']
                )
                if port_info['from'] == port_info['to']:
                    port_info['block'] = port_info['from']
                else:
                    port_info['block'] = '%s-%s' % (
                        port_info['from'],
                        port_info['to']
                    )

            port_info['policyGroupType'] = None
            port_info['policyGroupDn'] = None
            port_info['policyGroupName'] = None
            if 'infraRsAccBaseGrp' in port_mo and port_mo['infraRsAccBaseGrp'] is not None:
                port_info['policyGroupType'] = port_mo['infraRsAccBaseGrp']['tCl']
                port_info['policyGroupDn'] = port_mo['infraRsAccBaseGrp']['tDn']
                port_info['policyGroupName'] = '-'.join(port_info['policyGroupDn'].split('/')[-1].split('-')[1:])

            info['selector'].append(
                port_info
            )

        info['selector'] = sorted(
            info['selector'],
            key=lambda i: i['block']
        )

        return info

    def get_profiles_leaf_interface_info(self):
        if self.profile_leaf_interface is not None:
            return self.profile_leaf_interface

        profiles_mo = self.get_profile_leaf_interface_mo()
        if profiles_mo is None:
            return None

        self.profile_leaf_interface = []
        for profile_mo in profiles_mo:
            self.profile_leaf_interface.append(
                self.get_profile_leaf_interface_info(
                    profile_mo
                )
            )

        self.log.apic_mo(
            'leafInterfaceProfile.info',
            self.profile_leaf_interface
        )

        return self.profile_leaf_interface

    def match_profile_leaf_interface(self, profile_info, profile_filter):
        if profile_filter is None or len(profile_filter) == 0:
            return True

        for ap_rule in profile_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, profile_info['name']):
                    return False

        return True

    def get_profiles_leaf_interface(
            self,
            profile_filter=None,
            node_info=False,
            node_interface_info=False,
            reln_info=False
            ):
        all_profiles = self.get_profiles_leaf_interface_info()
        if all_profiles is None:
            return None

        profiles = []

        for profile_info in all_profiles:
            if not self.match_profile_leaf_interface(profile_info, profile_filter):
                continue

            if reln_info:
                profile_info['reln'] = self.get_profile_leaf_interface_reln_info(
                    profile_info['name']
                )

            if node_info or node_interface_info:
                profile_info['node_ids'] = self.get_profile_leaf_interface_node_ids(
                    profile_info['name']
                )

            if node_interface_info:
                profile_info['node_interfaces'] = []
                for node_id in profile_info['node_ids']:
                    profile_info['node_interfaces'] = profile_info['node_interfaces'] + self.get_profile_leaf_interface_node_interfaces_info(
                        profile_info['name'],
                        node_id
                    )

            profiles.append(
                profile_info
            )

        profiles = sorted(
            profiles,
            key=lambda i: i['name'].lower()
        )

        return profiles

    def get_profile_leaf_interface(self, name):
        profiles = self.get_profiles_leaf_interface(
            interface_filter=['name:%s' % (name)]
        )

        if profiles is None or len(profiles) != 1:
            return None

        return profiles[0]
