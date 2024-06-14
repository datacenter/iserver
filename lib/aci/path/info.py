from lib import filter_helper


class FabricPathInfo():
    def __init__(self):
        self.fabric_path = None

    def get_fabric_path_info(self, managed_object):
        #
        # Single Port
        #
        # "breakT": "nonbroken",
        # "childAction": "",
        # "descr": "",
        # "dn": "topology/pod-1/paths-205/pathep-[eth1/14]",
        # "lagT": "not-aggregated",
        # "lcOwn": "local",
        # "modTs": "2019-11-28T12:17:56.054+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "eth1/14",
        # "pathT": "leaf",
        # "status": ""
        #
        # Port Aggregation
        #
        # "breakT": "nonbroken",
        # "childAction": "",
        # "descr": "ACI1 UCSB1-FI-A Policy Group (Created by Ansible)",
        # "dn": "topology/pod-1/paths-206/pathep-[UCSB1-FI-A_PolGrp]",
        # "lagT": "node",
        # "lcOwn": "local",
        # "modTs": "2022-09-14T22:41:36.792+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "name": "UCSB1-FI-A_PolGrp",
        # "pathT": "leaf",
        # "status": ""
        info = {}
        info['__Output'] = {}

        keys = [
            'breakT',
            'dn',
            'lagT',
            'name',
            'pathT'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # External - not in scope and assumption is it will be not shown for local endpoint
        # "topology/pod-{id}/protpaths-{nodeAId}-{nodeBId}/extprotpaths-{extChAId}-{extChBId}/pathep-[{name}]",
        # "topology/pod-{id}/paths-{nodeId}/extpaths-{extChId}/pathep-[{name}]",

        # Internal
        # "topology/pod-{id}/protpaths-{nodeAId}-{nodeBId}/pathep-[{name}]",
        # "topology/pod-{id}/paths-{nodeId}/pathep-[{name}]"

        if info['lagT'] == 'not-aggregated':
            # "topology/pod-{id}/paths-{nodeId}/pathep-[{name}]"
            info['aggregate'] = False
            info['resolved'] = True
            info['policy_group_name'] = None
            info['ports'] = []
            port_info = {}
            port_info['pod_id'] = info['dn'].split('/')[1].split('-')[1]
            port_info['node_id'] = info['dn'].split('/')[2].split('-')[1]
            port_info['port_id'] = info['name']
            port_info['ep'] = 'pod-%s:node-%s:%s' % (
                port_info['pod_id'],
                port_info['node_id'],
                port_info['port_id']
            )
            info['ports'].append(port_info)

        else:
            # While both options are possible for dn format, the name will be of the policy group
            # "topology/pod-{id}/protpaths-{nodeAId}-{nodeBId}/pathep-[{name}]",
            # "topology/pod-{id}/paths-{nodeId}/pathep-[{name}]"
            info['aggregate'] = True
            info['resolved'] = False
            info['policy_group_name'] = info['name']
            info['ports'] = []
            port_info = {}
            port_info['ep'] = '(%s)' % (info['policy_group_name'])
            info['ports'].append(port_info)

        if info['lagT'] not in ['node', 'not-aggregated']:
            self.log.error(
                'get_fabric_path_info',
                'Unsupported fabric path: %s' % (managed_object)
            )

        return info

    def get_fabric_paths_info(self):
        if self.fabric_path is not None:
            return self.fabric_path

        managed_objects = self.get_fabric_path_mo()
        if managed_objects is None:
            return None

        self.fabric_path = []
        for managed_object in managed_objects:
            self.fabric_path.append(
                self.get_fabric_path_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'fabricPathEp.info',
            self.fabric_path
        )

        return self.fabric_path

    def match_fabric_path(self, fabric_path_info, fabric_path_filter):
        if fabric_path_filter is None or len(fabric_path_filter) == 0:
            return True

        for aepg_rule in fabric_path_filter:
            (key, value) = aepg_rule.split(':')

            if key == 'dn':
                if not filter_helper.match_string(value, fabric_path_info['dn']):
                    return False

        return True

    def get_fabric_paths(self, fabric_path_filter=None):
        all_paths = self.get_fabric_paths_info()

        fabric_paths = []

        for fabric_path_info in all_paths:
            if not self.match_fabric_path(fabric_path_info, fabric_path_filter):
                continue

            fabric_paths.append(fabric_path_info)

        return fabric_paths

    def get_fabric_path_by_dn(self, fabric_path_dn):
        fabric_paths = self.get_fabric_paths(
            fabric_path_filter=['dn:%s' % (fabric_path_dn)]
        )
        if fabric_paths is None:
            return None

        if len(fabric_paths) == 1:
            return fabric_paths[0]

        return None

    def get_fabric_path_ports(self, fabric_path_dn, resolve=False, phy=False):
        ports = []

        fabric_path = self.get_fabric_path_by_dn(fabric_path_dn)
        if fabric_path is not None:
            if fabric_path['resolved']:
                return fabric_path['ports']

            policy_group_nodes = self.get_policy_group_access_interface_vpc_nodes()
            for policy_group in policy_group_nodes:
                if policy_group['name'] == fabric_path['policy_group_name']:
                    if resolve:
                        for node in policy_group['nodes']:
                            node_ports = self.get_policy_group_access_interface_vpc_ports(
                                policy_group['name'],
                                node['id']
                            )
                            if node_ports is not None:
                                ports = ports + node_ports

                    if not resolve:
                        ports = []

                        for node in policy_group['nodes']:
                            port_info = {}
                            port_info['node_id'] = node['id']
                            port_info['ep'] = '(p) node-%s (%s)' % (
                                node['id'],
                                policy_group['name']
                            )
                            ports.append(port_info)

        return ports
