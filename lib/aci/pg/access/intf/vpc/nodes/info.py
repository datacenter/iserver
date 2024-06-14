from lib import filter_helper


class PolicyGroupAccessInterfaceVpcNodesInfo():
    def __init__(self):
        self.policy_group_access_interface_vpc_nodes = None

    def get_policy_group_access_interface_vpc_nodes_info(self, managed_object):
        # {
        #     "annotation": "orchestrator:terraform",
        #     "childAction": "",
        #     "descr": "k8s ESX72 vPC",
        #     "dn": "uni/infra/funcprof/accbundle-k8s_esx72_PolGrp",
        #     "extMngdBy": "",
        #     "lagT": "node",
        #     "lcOwn": "local",
        #     "modTs": "2022-12-12T20:45:32.634+01:00",
        #     "monPolDn": "uni/fabric/monfab-default",
        #     "name": "k8s_esx72_PolGrp",
        #     "nameAlias": "kali",
        #     "ownerKey": "",
        #     "ownerTag": "",
        #     "status": "",
        #     "uid": "15374",
        #     "userdom": ":all:common:",
        #     "pconsNodeDeployCtx": [
        #         {
        #             "childAction": "deleteNonPresent",
        #             "count": "0",
        #             "deployStatus": "deployed",
        #             "lcOwn": "local",
        #             "modTs": "never",
        #             "nodeId": "2208",
        #             "rn": "nctx-2208",
        #             "status": ""
        #         },
        #         {
        #             "childAction": "deleteNonPresent",
        #             "count": "0",
        #             "deployStatus": "deployed",
        #             "lcOwn": "local",
        #             "modTs": "never",
        #             "nodeId": "2207",
        #             "rn": "nctx-2207",
        #             "status": ""
        #         }
        #     ]
        # }
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

        info['nodes'] = []
        if 'pconsNodeDeployCtx' in managed_object:
            for node in managed_object['pconsNodeDeployCtx']:
                if node['deployStatus'] == 'deployed':
                    if node['nodeId'] not in info['nodes']:
                        node_info = {}
                        node_info['id'] = node['nodeId']
                        node_info['name'] = self.get_node_name(
                            node['nodeId']
                        )
                        info['nodes'].append(
                            node_info
                        )

        return info

    def get_policy_groups_access_interface_vpc_nodes_info(self):
        if self.policy_group_access_interface_vpc_nodes is not None:
            return self.policy_group_access_interface_vpc_nodes

        managed_objects = self.get_policy_group_access_interface_vpc_nodes_mo()
        if managed_objects is None:
            return None

        self.policy_group_access_interface_vpc_nodes = []
        for managed_object in managed_objects:
            self.policy_group_access_interface_vpc_nodes.append(
                self.get_policy_group_access_interface_vpc_nodes_info(
                    managed_object
                )
            )

        return self.policy_group_access_interface_vpc_nodes

    def match_policy_group_access_interface_vpc_nodes(self, policy_group_info, policy_group_filter):
        if policy_group_filter is None or len(policy_group_filter) == 0:
            return True

        for ap_rule in policy_group_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, policy_group_info['name']):
                    return False

        return True

    def get_policy_group_access_interface_vpc_nodes(self, policy_group_filter=None, port_info=False):
        all_policy_groups = self.get_policy_groups_access_interface_vpc_nodes_info()
        if all_policy_groups is None:
            return None

        policy_groups = []

        for policy_group_info in all_policy_groups:
            if not self.match_policy_group_access_interface_vpc_nodes(policy_group_info, policy_group_filter):
                continue

            if port_info:
                policy_group_info['ports'] = []
                for node_info in policy_group_info['nodes']:
                    ports_info = self.get_policy_group_access_interface_vpc_ports(
                        policy_group_info['name'],
                        node_info['id']
                    )
                    if ports_info is not None:
                        policy_group_info['ports'] = policy_group_info['ports'] + ports_info

            policy_groups.append(
                policy_group_info
            )

        policy_groups = sorted(
            policy_groups,
            key=lambda i: i['name'].lower()
        )

        return policy_groups
