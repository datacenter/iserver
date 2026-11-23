import copy
import json

from lib import ip_helper


class OcpNodeSriov():
    def __init__(self):
        self.node_sriov = {}

    def get_ocp_node_sriov_interfaces(self, node_name):
        if node_name in self.node_sriov:
            return self.node_sriov[node_name]

        linux_handler = self.get_ocp_node_linux_handler(
            node_name=node_name
        )
        if linux_handler is None:
            return None

        interfaces = linux_handler.get_sriov_interfaces(
            numa_info=True,
            pci_info=True
        )

        for interface in interfaces:
            for sriov_vf in interface['vf']:
                sriov_vf['policyName'] = ''

            interface['policy'] = []
            node_policies = self.k8s_handler.get_sriov_network_node_policies_with_interface(
                interface['name']
            )

            interface['numVfs'] = 0
            interface['vfCount'] = 0
            interface['vfNetwork'] = 0

            for node_policy in node_policies:
                node_policy_info = {}
                node_policy_info['name'] = node_policy['metadata']['name']
                node_policy_info['resourceName'] = node_policy['spec']['resourceName']
                node_policy_info['deviceType'] = node_policy['spec']['deviceType']
                node_policy_info['numVfs'] = node_policy['spec']['numVfs']
                node_policy_info['vfCount'] = node_policy['spec']['numVfs']
                node_policy_info['networks'] = []
                node_policy_info['selector'] = None
                if 'pfNames' not in node_policy['spec']['nicSelector']:
                    self.log.error(
                        'get_ocp_node_sriov_interfaces',
                        'Unsupported nicSelector: %s' % (node_policy['spec']['nicSelector'])
                    )

                if 'pfNames' in node_policy['spec']['nicSelector']:
                    for pf_name in node_policy['spec']['nicSelector']['pfNames']:
                        if len(pf_name.split('#')) == 1 and pf_name == interface['name']:
                            for sriov_vf in interface['vf']:
                                sriov_vf['policyName'] = node_policy_info['name']

                        if len(pf_name.split('#')) == 2 and pf_name.split('#')[0] == interface['name']:
                            node_policy_info['selector'] = pf_name
                            (start_vf, end_vf) = pf_name.split('#')[1].split('-')
                            node_policy_info['vfCount'] = int(end_vf) - int(start_vf) + 1

                            for sriov_vf in interface['vf']:
                                if int(start_vf) <= int(sriov_vf['index']) <= int(end_vf):
                                    sriov_vf['policyName'] = node_policy_info['name']

                networks = self.k8s_handler.get_sriov_networks_with_resource_name(
                    node_policy_info['resourceName'],
                    return_mo=True
                )
                if networks is not None:
                    for network in networks:
                        network_info = {}
                        network_info['__Output'] = {}
                        network_info['name'] = network['metadata']['name']
                        network_info['namespace'] = network['metadata']['namespace']
                        network_info['networkNamespace'] = network['spec']['networkNamespace']
                        network_info['namespace_name'] = '%s/%s' % (
                            network_info['networkNamespace'],
                            network_info['name']
                        )
                        network_info['ipam'] = None
                        if 'ipam' in network['spec']:
                            try:
                                network_info['ipam'] = json.loads(
                                    network['spec']['ipam']
                                )
                            except BaseException:
                                network_info['ipam'] = network['spec']['ipam']

                        if network_info['ipam'] is None:
                            network_info['ipamTick'] = '\u2717'
                            network_info['__Output']['ipamTick'] = 'Red'
                        else:
                            network_info['ipamTick'] = '\u2713'
                            network_info['__Output']['ipamTick'] = 'Green'

                        network_info['vlan'] = '--'
                        if 'vlan' in network['spec']:
                            network_info['vlan'] = network['spec']['vlan']

                        node_policy_info['networks'].append(
                            network_info
                        )

                node_policy_info['networksCount'] = len(node_policy_info['networks'])
                node_policy_info['vfUsage'] = '%s/%s' % (
                    node_policy_info['networksCount'],
                    node_policy_info['vfCount']
                )

                interface['numVfs'] = node_policy_info['numVfs']
                interface['vfCount'] = interface['vfCount'] + node_policy_info['vfCount']
                interface['vfNetwork'] = interface['vfNetwork'] + node_policy_info['networksCount']

                interface['policy'].append(
                    node_policy_info
                )

            interface['vfUsage'] = '%s/%s' % (
                interface['vfNetwork'],
                interface['vfCount']
            )
            interface['policyCount'] = len(
                interface['policy']
            )

        self.node_sriov[node_name] = interfaces
        self.log.debug(
            'get_ocp_node_sriov_interfaces',
            json.dumps(interfaces, indent=4)
        )

        return interfaces

    def get_ocp_node_sriov_phy(self, node_name):
        interfaces = self.get_ocp_node_sriov_interfaces(
            node_name
        )
        if interfaces is None:
            return None

        info = []
        for interface in interfaces:
            interface_info = {}
            interface_info['__Output'] = {}
            interface_info['name'] = interface['name']
            interface_info['flags'] = interface['flags']
            interface_info['mtu'] = interface['mtu']
            interface_info['state'] = interface['state']
            if interface_info['state'].lower() == 'up':
                interface_info['__Output']['state'] = 'Green'
            else:
                interface_info['__Output']['state'] = 'Red'
            interface_info['mac'] = interface['mac']
            interface_info['numa'] = interface['numa']
            interface_info['pci'] = interface['pci']
            interface_info['numVfs'] = interface['numVfs']
            interface_info['vfUsage'] = interface['vfUsage']
            interface_info['policyCount'] = interface['policyCount']
            info.append(
                interface_info
            )

        info = sorted(
            info,
            key=lambda i: i['name']
        )

        return info

    def get_ocp_node_sriov_policy(self, node_name):
        interfaces = self.get_ocp_node_sriov_interfaces(
            node_name
        )
        if interfaces is None:
            return None

        info = []
        for interface in interfaces:
            for policy in interface['policy']:
                interface_info = {}
                interface_info['__Output'] = {}
                interface_info['name'] = interface['name']
                interface_info['policyName'] = policy['name']
                interface_info['resourceName'] = policy['resourceName']
                interface_info['deviceType'] = policy['deviceType']
                interface_info['numVfs'] = policy['numVfs']
                interface_info['selector'] = policy['selector']
                interface_info['vfUsage'] = policy['vfUsage']
                info.append(
                    interface_info
                )

        info = sorted(
            info,
            key=lambda i: i['policyName']
        )

        return info

    def get_ocp_node_sriov_network(self, node_name):
        interfaces = self.get_ocp_node_sriov_interfaces(
            node_name
        )
        if interfaces is None:
            return None

        info = []
        for interface in interfaces:
            for policy in interface['policy']:
                for network in policy['networks']:
                    network_info = copy.deepcopy(network)
                    network_info['interfaceName'] = interface['name']
                    network_info['policyName'] = policy['name']
                    network_info['resourceName'] = policy['resourceName']
                    network_info['deviceType'] = policy['deviceType']
                    network_info['selector'] = policy['selector']
                    network_info['vf'] = ''
                    network_info['usedBy'] = ''

                    vm_filter = ['multus_network:%s' % (network_info['name'])]
                    ocp_vms = self.get_ocp_vms(vm_filter=vm_filter)
                    if ocp_vms is not None and len(ocp_vms) == 1:
                        network_info['usedBy'] = 'VM: %s' % (
                            ocp_vms[0]['namespace_name']
                        )
                        for vm_interface in ocp_vms[0]['interfaces']:
                            if vm_interface['multusNetworkName'] == network_info['name']:
                                network_info['usedBy'] = '%s/%s' % (
                                    network_info['usedBy'],
                                    vm_interface['name']
                                )
                                for interface_vf in interface['vf']:
                                    if ip_helper.is_mac_equal(interface_vf['mac'], vm_interface['mac_address']):
                                        network_info['vf'] = interface_vf['index']

                    pod_filter = ['network:%s' % (network_info['namespace_name'])]
                    ocp_pods = self.k8s_handler.get_pods(pod_filter=pod_filter)
                    if ocp_pods is not None and len(ocp_pods) == 1:
                        network_info['usedBy'] = 'POD: %s/%s' % (
                            ocp_pods[0]['metadata']['namespace'],
                            ocp_pods[0]['metadata']['name']
                        )
                        for pod_interface in ocp_pods[0]['networks']:
                            if pod_interface['name'] == network_info['namespace_name']:
                                network_info['usedBy'] = '%s/%s' % (
                                    network_info['usedBy'],
                                    pod_interface['interface']
                                )
                                for interface_vf in interface['vf']:
                                    if ip_helper.is_mac_equal(interface_vf['mac'], pod_interface['mac']):
                                        network_info['vf'] = interface_vf['index']

                    info.append(
                        network_info
                    )

        info = sorted(
            info,
            key=lambda i: i['namespace_name']
        )

        return info

    def get_ocp_node_sriov_vf(self, node_name):
        interfaces = self.get_ocp_node_sriov_interfaces(
            node_name
        )
        if interfaces is None:
            return None

        info = []
        for interface in interfaces:
            for sriov_vf in interface['vf']:
                interface_info = {}
                interface_info['__Output'] = {}
                interface_info['name'] = interface['name']
                interface_info['index'] = sriov_vf['index']
                interface_info['mac'] = sriov_vf['mac']
                interface_info['vlan'] = '--'
                if sriov_vf['vlan'] is not None:
                    interface_info['vlan'] = sriov_vf['vlan']
                interface_info['spoof'] = sriov_vf['spoof']
                interface_info['link'] = sriov_vf['link']
                interface_info['trust'] = sriov_vf['trust']
                interface_info['policyName'] = sriov_vf['policyName']

                interface_info['used'] = False
                interface_info['usedTick'] = '\u2717'
                interface_info['networkName'] = ''
                interface_info['__Output']['usedTick'] = 'Red'
                interface_info['usedBy'] = ''

                vm_filter = ['mac:%s' % (sriov_vf['mac'])]
                ocp_vms = self.get_ocp_vms(vm_filter=vm_filter)
                if ocp_vms is not None and len(ocp_vms) == 1:
                    interface_info['used'] = True
                    interface_info['usedTick'] = '\u2713'
                    interface_info['__Output']['usedTick'] = 'Green'
                    interface_info['usedBy'] = 'VM: %s' % (
                        ocp_vms[0]['namespace_name']
                    )
                    for vm_interface in ocp_vms[0]['interfaces']:
                        if ip_helper.is_mac_equal(vm_interface['mac_address'], sriov_vf['mac']):
                            interface_info['networkName'] = vm_interface['multusNetworkName']
                            interface_info['usedBy'] = '%s/%s' % (
                                interface_info['usedBy'],
                                vm_interface['name']
                            )

                pod_filter = ['mac:%s' % (sriov_vf['mac'])]
                ocp_pods = self.k8s_handler.get_pods(pod_filter=pod_filter)
                if ocp_pods is not None and len(ocp_pods) == 1:
                    interface_info['used'] = True
                    interface_info['usedTick'] = '\u2713'
                    interface_info['__Output']['usedTick'] = 'Green'
                    interface_info['usedBy'] = 'POD: %s/%s' % (
                        ocp_pods[0]['metadata']['namespace'],
                        ocp_pods[0]['metadata']['name']
                    )
                    for pod_interface in ocp_pods[0]['networks']:
                        if ip_helper.is_mac_equal(pod_interface['mac'], sriov_vf['mac']):
                            interface_info['networkName'] = pod_interface['name']
                            interface_info['usedBy'] = '%s/%s' % (
                                interface_info['usedBy'],
                                pod_interface['interface']
                            )

                info.append(
                    interface_info
                )

        return info

    def get_ocp_node_sriov(self, node_name, sriov_phy_info=False, sriov_policy_info=False, sriov_network_info=False, sriov_vf_info=False):
        info = {}

        if sriov_phy_info:
            info['sriov_phy'] = self.get_ocp_node_sriov_phy(
                node_name
            )

        if sriov_policy_info:
            info['sriov_policy'] = self.get_ocp_node_sriov_policy(
                node_name
            )

        if sriov_network_info:
            info['sriov_network'] = self.get_ocp_node_sriov_network(
                node_name
            )

        if sriov_vf_info:
            info['sriov_vf'] = self.get_ocp_node_sriov_vf(
                node_name
            )

        return info
