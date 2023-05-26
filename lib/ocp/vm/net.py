import json

from lib.xd import aci


class OcpVmNet():
    def __init__(self):
        pass

    def get_ocp_vm_sriov_net_fabric_info(self, sriov_network_name, mac_address):
        sriov_network_mo = self.get_ocp_sriov_network(
            'openshift-sriov-network-operator',
            sriov_network_name
        )
        if sriov_network_mo is None:
            return None

        if 'labels' not in sriov_network_mo['metadata']:
            return None

        if 'fabric_type' not in sriov_network_mo['metadata']['labels']:
            return None

        if 'fabric_name' not in sriov_network_mo['metadata']['labels']:
            return None

        if sriov_network_mo['metadata']['labels']['fabric_type'] == 'aci':
            endpoints = aci.get_aci_endpoints(
                macs=[mac_address],
                apic_ips=[sriov_network_mo['metadata']['labels']['fabric_name']]
            )
            return endpoints

        return None

    def get_ocp_vm_net_info(self, namespace, name):
        info = self.get_ocp_vms_info(
            name=name,
            namespace=namespace
        )
        if info is None:
            return None

        pod_mo = self.k8s_handler.get_pod_with_label(
            'kubevirt.io/domain',
            name,
            namespace=namespace
        )

        linux_handler = self.get_ocp_node_linux_handler(
            pod_mo['status']['host_ip']
        )

        for interface in info['interfaces']:
            interface['__Output'] = {}
            interface['info'] = {}
            interface['info']['host_interface'] = None
            interface['ips'] = []

            order = 0
            for network in info['networks']:
                if network['name'] == interface['name']:
                    interface['info']['order'] = order
                    if network['pod'] is not None:
                        interface['info']['network_name'] = 'Pod networking'
                        if interface['masquerade'] is not None:
                            interface['info']['network_type'] = 'Masquerade'

                    if network['multus'] is not None:
                        interface['info']['network_name'] = network['multus']['network_name']
                        if interface['sriov'] is not None:
                            interface['info']['network_type'] = 'SR-IOV'
                            if linux_handler is not None:
                                interface['info']['host_interface'] = linux_handler.get_interface(
                                    interface['mac_address'],
                                    cache=True
                                )

                            interface['endpoints'] = self.get_ocp_vm_sriov_net_fabric_info(
                                network['multus']['network_name'],
                                interface['mac_address']
                            )

                        else:
                            interface['info']['network_type'] = 'Multus'

                    break

                order = order + 1

            if pod_mo is not None:
                for networks_status in json.loads(pod_mo['metadata']['annotations']['k8s.v1.cni.cncf.io/networks-status']):
                    if interface['info']['order'] == 0 and networks_status['interface'] == 'eth0':
                        interface['ips'] = networks_status['ips']
                        interface['info']['pci'] = ''
                        break

                    if 'net%s' % (interface['info']['order']) == networks_status['interface']:
                        interface['ips'] = None
                        if 'ips' in networks_status:
                            interface['ips'] = networks_status['ips']

                        interface['info']['pci'] = ''
                        if interface['sriov'] is not None:
                            if networks_status['device-info']['type'] == 'pci':
                                interface['info']['pci'] = networks_status['device-info']['pci']['pci-address']

                        break

        return info

    def print_ocp_vm_net_info(self, info, show_vm_info=True, stream='default'):
        if show_vm_info:
            self.print_ocp_vm_base_info(info, stream=stream)

        order = [
            'name',
            'info.order',
            'info.network_type',
            'info.network_name',
            'ips',
            'mac_address',
            'info.pci',
            'info.host_interface.name',
            'info.host_interface.vf_info.index',
            'info.host_interface.vf_info.vlan'
        ]

        headers = [
            'Name',
            'Order',
            'Type',
            'Network',
            'IP',
            'MAC',
            'PCI',
            'Host Interface',
            'VF ID',
            'VF VLAN'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info['interfaces'],
                order,
                ['ips']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True,
            stream=stream
        )
