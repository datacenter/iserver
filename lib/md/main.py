import os
import shutil
import datetime
import copy
from lib import file_helper
from lib import output_helper
from lib.xd import main as xd
from lib.md.aci.main import MdAciOutput
from lib.md.cnc.main import MdCncOutput
from lib.md.compute.main import MdComputeOutput
from lib.md.fi.main import MdFiOutput
from lib.md.k8s.main import MdK8sOutput
from lib.md.nexus.main import MdNexusOutput
from lib.md.serial import MdSerialOutput
from lib.md.vc.main import MdVcOutput


class Md(
        MdAciOutput,
        MdCncOutput,
        MdComputeOutput,
        MdFiOutput,
        MdK8sOutput,
        MdNexusOutput,
        MdSerialOutput,
        MdVcOutput
        ):
    def __init__(self, domain_name, md_directory, log_id=None):
        MdAciOutput.__init__(self)
        MdCncOutput.__init__(self)
        MdComputeOutput.__init__(self)
        MdFiOutput.__init__(self)
        MdK8sOutput.__init__(self)
        MdNexusOutput.__init__(self)
        MdSerialOutput.__init__(self)
        MdVcOutput.__init__(self)

        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.md_directory = md_directory
        self.domain_name = domain_name
        self.xd_handler = xd.CrossDomain(log_id=log_id, debug=True)
        self.server_tag_count = {}
        self.fi_names_hash = {}
        self.fi_eth_count = {}
        self.fi_eth_up_count = {}
        self.fi_eth_config_count = {}
        self.fi_pc_count = {}
        self.fi_pc_up_count = {}
        self.fi_server_count = {}
        self.fi_vmware_count = {}
        self.fi_ocp_count = {}
        self.nexus_device_names = None
        self.nexus_fabric_server_count = 0
        self.nexus_fabric_server_intf_count = 0
        self.nexus_fabric_vcenter_count = {}
        self.nexus_fabric_vcenter_intf_count = {}
        self.nexus_eth_count = {}
        self.nexus_eth_up_count = {}
        self.nexus_pc_count = {}
        self.nexus_vlan_count = {}
        self.nexus_server_count = {}
        self.nexus_vmware_count = {}
        self.nexus_ocp_count = {}
        self.nexus_lldp_count = {}
        self.nexus_cdp_count = {}
        self.nexus_mac_count = {}
        self.nexus_hw = {}
        self.aci_controller_names = []
        self.aci_tenant_names = {}
        self.aci_tenant_count = {}
        self.aci_ap_count = {}
        self.aci_bd_count = {}
        self.aci_epg_count = {}
        self.aci_vrf_count = {}
        self.aci_l2out_count = {}
        self.aci_l3mpls_count = {}
        self.aci_l3out_count = {}
        self.aci_aae_count = {}
        self.aci_pool_vlan_count = {}
        self.aci_domain_aaa_count = {}
        self.aci_domain_l2_count = {}
        self.aci_domain_l3_count = {}
        self.aci_domain_phy_count = {}
        self.aci_domain_vmm_count = {}
        self.aci_contract_filter_count = {}
        self.aci_contract_standard_count = {}
        self.aci_contract_taboo_count = {}
        self.aci_node_names = {}
        self.aci_node_mapping = {}
        self.aci_server_count = {}
        self.aci_vmware_count = {}
        self.aci_ocp_count = {}
        self.aci_ep_count = {}
        self.aci_lacp_count = {}
        self.aci_lldp_count = {}
        self.aci_cdp_count = {}
        self.aci_bgp_count = {}
        self.aci_node_server_count = {}
        self.aci_node_vmware_count = {}
        self.aci_node_ocp_count = {}
        self.aci_node_phy_count = {}
        self.aci_node_phy_up_count = {}
        self.aci_node_lacp_count = {}
        self.aci_node_lldp_count = {}
        self.aci_node_cdp_count = {}
        self.aci_node_bgp_count = {}
        self.vc_hw_count = {}
        self.vc_nic_count = {}
        self.vc_nic_up_count = {}
        self.vc_vnic_count = {}
        self.vc_vnic_up_count = {}
        self.vc_switch_count = {}
        self.vc_switch_up_count = {}
        self.vc_dvs_count = {}
        self.vc_dvs_up_count = {}
        self.vc_net_count = {}
        self.vc_net_up_count = {}
        self.vc_vm_count = {}
        self.vc_vm_up_count = {}
        self.debug = True

    def initialize(self):
        self.fi_names_hash = self.xd_handler.get_fi_device_names_hash()
        for name in self.fi_names_hash:
            self.fi_eth_up_count[name] = 0
            self.fi_eth_config_count[name] = 0
            self.fi_eth_count[name] = 0
            self.fi_pc_up_count[name] = 0
            self.fi_pc_count[name] = 0
            self.fi_server_count[name] = 0
            self.fi_vmware_count[name] = 0
            self.fi_ocp_count[name] = 0

        self.nexus_device_names = self.xd_handler.get_nexus_device_names()
        for name in self.nexus_device_names:
            self.nexus_eth_count[name] = 0
            self.nexus_pc_count[name] = 0
            self.nexus_vlan_count[name] = 0
            self.nexus_server_count[name] = 0
            self.nexus_vmware_count[name] = 0
            self.nexus_ocp_count[name] = 0
            self.nexus_cdp_count[name] = 0
            self.nexus_lldp_count[name] = 0
            self.nexus_mac_count[name] = 0

        for key in self.xd_handler.vc_instance:
            self.vc_hw_count[key] = {}
            self.vc_nic_count[key] = {}
            self.vc_nic_up_count[key] = {}
            self.vc_vnic_count[key] = {}
            self.vc_vnic_up_count[key] = {}
            self.vc_switch_count[key] = {}
            self.vc_switch_up_count[key] = {}
            self.vc_dvs_count[key] = {}
            self.vc_dvs_up_count[key] = {}
            self.vc_net_count[key] = {}
            self.vc_net_up_count[key] = {}
            self.vc_vm_count[key] = {}
            self.vc_vm_up_count[key] = {}

        self.aci_controller_names = self.xd_handler.get_aci_names()
        for name in self.aci_controller_names:
            self.aci_tenant_names[name] = self.xd_handler.get_aci_tenant_names(name)
            self.aci_server_count[name] = 0
            self.aci_vmware_count[name] = 0
            self.aci_ocp_count[name] = 0
            self.aci_tenant_count[name] = 0
            self.aci_ap_count[name] = 0
            self.aci_bd_count[name] = 0
            self.aci_epg_count[name] = 0
            self.aci_vrf_count[name] = 0
            self.aci_l2out_count[name] = 0
            self.aci_l3mpls_count[name] = 0
            self.aci_l3out_count[name] = 0
            self.aci_aae_count[name] = 0
            self.aci_pool_vlan_count[name] = 0
            self.aci_domain_aaa_count[name] = 0
            self.aci_domain_l2_count[name] = 0
            self.aci_domain_l3_count[name] = 0
            self.aci_domain_phy_count[name] = 0
            self.aci_domain_vmm_count[name] = 0
            self.aci_contract_filter_count[name] = 0
            self.aci_contract_standard_count[name] = 0
            self.aci_contract_taboo_count[name] = 0
            self.aci_ep_count[name] = 0
            self.aci_lacp_count[name] = 0
            self.aci_lldp_count[name] = 0
            self.aci_cdp_count[name] = 0
            self.aci_bgp_count[name] = 0

        self.aci_node_names = self.xd_handler.get_aci_node_names()
        for name in self.aci_controller_names:
            self.aci_node_server_count[name] = {}
            self.aci_node_vmware_count[name] = {}
            self.aci_node_ocp_count[name] = {}
            self.aci_node_phy_count[name] = {}
            self.aci_node_phy_up_count[name] = {}
            self.aci_node_lacp_count[name] = {}
            self.aci_node_lldp_count[name] = {}
            self.aci_node_cdp_count[name] = {}
            self.aci_node_bgp_count[name] = {}
            for node in self.aci_node_names[name]:
                self.aci_node_server_count[name][node] = 0
                self.aci_node_vmware_count[name][node] = 0
                self.aci_node_ocp_count[name][node] = 0
                self.aci_node_phy_count[name][node] = 0
                self.aci_node_phy_up_count[name][node] = 0
                self.aci_node_lacp_count[name][node] = 0
                self.aci_node_lldp_count[name][node] = 0
                self.aci_node_cdp_count[name][node] = 0
                self.aci_node_bgp_count[name][node] = 0

    def print_table_header(self, order):
        line = ''
        line2 = ''
        for key in order:
            line = '%s %s |' % (line, key)
            line2 = '%s --- |' % (line2)
        line = line.rstrip('|')
        line2 = line2.rstrip('|')

        self.my_output.print_stream(line, 'output')
        self.my_output.print_stream(line2, 'output')

    def add_column_tick_string(self, line, value, check, last=False):
        if value is None or value != check:
            return self.add_column(line, ':x:', last=last)
        return self.add_column(line, ':white_check_mark:', last=last)

    def add_column_tick_bool(self, line, value, last=False):
        if value is None:
            return self.add_column(line, '---', last=last)
        if not value:
            return self.add_column(line, ':x:', last=last)
        return self.add_column(line, ':white_check_mark:', last=last)

    def add_column_tick_not_none(self, line, value, last=False):
        if value is None:
            return self.add_column(line, ':x:', last=last)
        return self.add_column(line, ':white_check_mark:', last=last)

    def add_column(self, row, value, last=False, mapping=True):
        first = False
        if len(row) == 0:
            first = True

        if mapping:
            if value is None:
                value = '---'

            if isinstance(value, str):
                if len(value) == 0 or value.lower() == 'none':
                    value = '---'

        if value is not None:
            if isinstance(value, str):
                value = value.replace('|', '\\|')

        if first:
            row = '%s' % (value)
        else:
            row = '%s %s' % (row, value)

        if not last:
            row = '%s |' % (row)

        return row

    def print_row_t2v(self, title, param, values1, values2):
        line = ''
        line = self.add_column(line, title)
        if values1 is None or param not in values1:
            line = self.add_column(line, '---')
        else:
            line = self.add_column(line, values1[param])

        if values2 is None or param not in values2:
            line = self.add_column(line, '---', last=True)
        else:
            line = self.add_column(line, values2[param])

        self.my_output.print_stream(line, 'output')

    def get_xd_device_link(self, item_xd, nei='cdp', short_names=True):
        output = None

        if item_xd['DeviceType'] is not None and item_xd['DeviceType'] == 'Server':
            if short_names:
                output = '[%s](../compute/%s-net.md)' % (
                    self.get_short_name(item_xd['ServerName']),
                    item_xd['ServerMoid']
                )
            else:
                output = '[%s](../compute/%s-net.md)' % (
                    item_xd['ServerName'],
                    item_xd['ServerMoid']
                )

        if item_xd['DeviceType'] is not None and item_xd['DeviceType'] == 'Nexus':
            nexus_name = item_xd['DeviceSysName']
            if short_names:
                nexus_name = self.get_short_name(
                    item_xd['DeviceSysName']
                )

            if item_xd['NexusDevice'] is None:
                output = '%s' % (
                    nexus_name
                )
            else:
                output = '[%s](../nexus/%s-%s.md)' % (
                    nexus_name,
                    item_xd['NexusDevice'],
                    nei
                )

        if item_xd['DeviceType'] is not None and item_xd['DeviceType'] == 'FI':
            if self.xd_handler.is_fi_name(item_xd['FI']):
                output = '[%s](../fi/%s-eth.md)' % (
                    item_xd['FI'],
                    self.xd_handler.get_fi_hash(item_xd['FI'])
                )
            else:
                output = '%s' % (
                    item_xd['FI']
                )

        if item_xd['DeviceType'] is not None and item_xd['DeviceType'] == 'ACI':
            node_name = item_xd['DeviceSysName']
            if short_names:
                node_name = self.get_short_name(
                    item_xd['DeviceSysName']
                )

            if item_xd['AciNodeName'] is None:
                output = '%s' % (
                    node_name
                )
            else:
                output = '[%s](../apic/%s-%s.md)' % (
                    item_xd['AciNodeName'],
                    item_xd['AciNodeRef'],
                    nei
                )

        return output

    def get_interface_dn(self, dn):
        dn = dn.replace('sys/rack-unit-1/', '')
        dn = dn.replace('adaptor-', 'slot-')
        dn = dn.replace('network-adapter-', 'slot-')
        return dn

    def get_adapter_model(self, model):
        model = model.replace('Cisco(R) Ethernet Converged ', '')
        model = model.replace('Cisco(R) LOM ', '')

        if model == 'Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC':
            model = 'Intel X710-DA4'

        if model == 'Cisco(R) Ethernet Converged NIC XXV710-DA2':
            model = 'Cisco XXV710-DA2'

        if model == 'Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC':
            model = 'Intel XL710-QDA2'

        return model

    def get_output_filename(self, name, subdir=None, extension='md'):
        directory = self.md_directory
        if subdir is not None:
            directory = self.md_directory
            for item in subdir.split('/'):
                directory = os.path.join(
                    directory,
                    item
                )

            if not os.path.isdir(directory):
                os.makedirs(directory, exist_ok=True)

        if extension is None:
            filename = os.path.join(
                directory,
                name
            )
        else:
            filename = os.path.join(
                directory,
                '%s.%s' % (name, extension)
            )

        return filename

    def convert_age(self, seconds):
        if seconds > 60 * 60 * 24:
            return '%sd' % (int(seconds / (60 * 60 * 24)))

        if seconds > 60 * 60:
            hours = 0
            while True:
                if seconds < 60 * 60:
                    break

                hours = hours + 1
                seconds = seconds - 60 * 60

            return '%sh%sm' % (
                hours,
                int(seconds / 60)
            )

        if seconds > 60:
            return '%sm' % (int(seconds / 60))

        return '%ss' % (seconds)

    def print_page_header(self, title, main_page=False):
        self.my_output.clear_output()

        self.my_output.print_stream(
            '# %s\n' % (title),
            'output'
        )

        if len(self.xd_handler.out_of_sync) > 0:
            self.my_output.print_stream(
                'Data collected:  %s CET [Out-of-sync](./out_of_sync.md)\n' % (
                    datetime.datetime.fromtimestamp(self.xd_handler.timestamp).strftime('%Y-%m-%d %H:%M:%S')
                ),
                'output'
            )
        else:
            self.my_output.print_stream(
                'Data collected:  %s CET\n' % (
                    datetime.datetime.fromtimestamp(self.xd_handler.timestamp).strftime('%Y-%m-%d %H:%M:%S')
                ),
                'output'
            )

    def save_output(self, name, subdir=None):
        file_helper.set_file(
            self.get_output_filename(name, subdir=subdir),
            self.my_output.get_output()
        )

    def copy_file(self, source, name, subdir=None):
        destination = self.get_output_filename(name, subdir=subdir, extension=None)
        shutil.copyfile(source, destination)

    def print_readme_server(self):
        self.my_output.print_stream(
            '## Server\n',
            'output'
        )

        self.my_output.print_stream(
            '\nServers | List | MAC | Fabric | NX | ACI',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | ---',
            'output'
        )

        self.my_output.print_stream(
            'All | [#%s](server-all.md) | [#%s](server-all-mac.md) | [#%s](server-all-fabric.md) | [#%s](server-all-nexus.md) | [#%s](server-all-aci.md)' % (
                self.server_tag_count['all'],
                self.server_tag_count['all-mac'],
                self.server_tag_count['all-fabric'],
                self.server_tag_count['all-nexus'],
                self.server_tag_count['all-aci']
            ),
            'output'
        )

        self.my_output.print_stream(
            'iConn\'d | [#%s](server-connected.md) | [#%s](server-connected-mac.md) | [#%s](server-connected-fabric.md) | [#%s](server-connected-nexus.md) | [#%s](server-connected-aci.md)' % (
                self.server_tag_count['connected'],
                self.server_tag_count['connected-mac'],
                self.server_tag_count['connected-fabric'],
                self.server_tag_count['connected-nexus'],
                self.server_tag_count['connected-aci']
            ),
            'output'
        )

        self.my_output.print_stream(
            'iDisc\'d | [#%s](server-disconnected.md) | [#%s](server-disconnected-mac.md) | [#%s](server-disconnected-fabric.md) | [#%s](server-disconnected-nexus.md) | [#%s](server-disconnected-aci.md)' % (
                self.server_tag_count['disconnected'],
                self.server_tag_count['disconnected-mac'],
                self.server_tag_count['disconnected-fabric'],
                self.server_tag_count['disconnected-nexus'],
                self.server_tag_count['disconnected-aci']
            ),
            'output'
        )

        self.my_output.print_stream(
            'vCenter | [#%s](server-vc-spdc.md) | [#%s](server-vc-spdc-mac.md) | [#%s](server-vc-spdc-fabric.md) | [#%s](server-vc-spdc-nexus.md) | [#%s](server-vc-spdc-aci.md)' % (
                self.server_tag_count['vc-spdc'],
                self.server_tag_count['vc-spdc-mac'],
                self.server_tag_count['vc-spdc-fabric'],
                self.server_tag_count['vc-spdc-nexus'],
                self.server_tag_count['vc-spdc-aci']
            ),
            'output'
        )

        for key in self.xd_handler.ocp:
            try:
                self.my_output.print_stream(
                    'ocp:%s | [#%s](server-ocp-%s.md) | [#%s](server-ocp-%s-mac.md) | [#%s](server-ocp-%s-fabric.md) | [#%s](server-ocp-%s-nexus.md) | [#%s](server-ocp-%s-aci.md)' % (
                        key,
                        self.server_tag_count['ocp-%s' % (key)],
                        key,
                        self.server_tag_count['ocp-%s-mac' % (key)],
                        key,
                        self.server_tag_count['ocp-%s-fabric' % (key)],
                        key,
                        self.server_tag_count['ocp-%s-nexus' % (key)],
                        key,
                        self.server_tag_count['ocp-%s-aci' % (key)],
                        key
                    ),
                    'output'
                )
            except BaseException:
                pass

    def print_readme_openshift(self):
        self.my_output.print_stream(
            '\n## OpenShift\n',
            'output'
        )

        self.my_output.print_stream(
            'Cluster | OCP | Kube | CNI | Node',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- ',
            'output'
        )

        for key in self.xd_handler.k8s_clusters:
            self.my_output.print_stream(
                '[%s](./ocp/cluster-%s.md) | %s | %s | [%s](./ocp/cni-%s.md) | [#%s](./ocp/nodes-%s.md)' % (
                    key,
                    key,
                    self.xd_handler.get_k8s_version_ocp(key),
                    self.xd_handler.get_k8s_version_kube(key),
                    self.xd_handler.get_k8s_cni_type(key),
                    key,
                    self.xd_handler.k8s_node_counts[key],
                    key
                ),
                'output'
            )

    def print_readme_vmware(self):
        self.my_output.print_stream(
            '\n## VMWare\n',
            'output'
        )

        order = [
            'vCenter',
            'Host / Cluster',
            'NIC',
            'VMk',
            'Net',
            'vSwitch',
            'DVS',
            'VM'
        ]
        self.print_table_header(order)

        for key in self.xd_handler.vc_instance:
            line = ''
            line = self.add_column(line, key)
            line = self.add_column(
                line,
                '[ALL](./vc/%s-hosts.md)' % (key)
            )
            line = self.add_column(line, '---')
            line = self.add_column(line, '---')
            line = self.add_column(
                line,
                '[%s/%s](./vc/%s-net.md)' % (
                    self.vc_net_up_count[key]['__ALL__'],
                    self.vc_net_count[key]['__ALL__'],
                    key
                )
            )
            line = self.add_column(line, '---')
            line = self.add_column(
                line,
                '[%s/%s](./vc/%s-dvs.md)' % (
                    self.vc_dvs_up_count[key]['__ALL__'],
                    self.vc_dvs_count[key]['__ALL__'],
                    key
                )
            )
            line = self.add_column(
                line,
                '[%s/%s](./vc/%s-vm.md)' % (
                    self.vc_vm_up_count[key]['__ALL__'],
                    self.vc_vm_count[key]['__ALL__'],
                    key
                )
            )
            self.my_output.print_stream(line, 'output')

            clusters = self.xd_handler.get_vc_cluster(key)
            if clusters is not None:
                for cluster in clusters:
                    line = ''
                    line = self.add_column(line, key)
                    line = self.add_column(
                        line,
                        '[%s](./vc/cluster/%s.md)' % (cluster['_name'], cluster['hash'])
                    )
                    line = self.add_column(
                        line,
                        '---'
                    )
                    line = self.add_column(
                        line,
                        '---'
                    )
                    line = self.add_column(
                        line,
                        '---'
                    )
                    line = self.add_column(
                        line,
                        '---'
                    )
                    line = self.add_column(
                        line,
                        '---'
                    )
                    line = self.add_column(
                        line,
                        '[%s/%s](./vc/vm/%s.md)' % (
                            self.vc_vm_up_count[key][cluster['name']],
                            self.vc_vm_count[key][cluster['name']],
                            cluster['hash']
                        )
                    )
                    self.my_output.print_stream(line, 'output')

            hosts = self.xd_handler.get_vc_host(key)
            if hosts is not None:
                for host in hosts:
                    line = ''
                    line = self.add_column(line, key)
                    if host['_ready']:
                        line = self.add_column(
                            line,
                            '[%s](./vc/host/%s.md)' % (host['_name'], host['hash'])
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/nic/%s.md)' % (
                                self.vc_nic_up_count[key][host['name']],
                                self.vc_nic_count[key][host['name']],
                                host['hash']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/vnic/%s.md)' % (
                                self.vc_vnic_up_count[key][host['name']],
                                self.vc_vnic_count[key][host['name']],
                                host['hash']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/net/%s.md)' % (
                                self.vc_net_up_count[key][host['name']],
                                self.vc_net_count[key][host['name']],
                                host['hash']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/switch/%s.md)' % (
                                self.vc_switch_up_count[key][host['name']],
                                self.vc_switch_count[key][host['name']],
                                host['hash']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/dvs/%s.md)' % (
                                self.vc_dvs_up_count[key][host['name']],
                                self.vc_dvs_count[key][host['name']],
                                host['hash']
                            )
                        )
                        line = self.add_column(
                            line,
                            '[%s/%s](./vc/vm/%s.md)' % (
                                self.vc_vm_up_count[key][host['name']],
                                self.vc_vm_count[key][host['name']],
                                host['hash']
                            )
                        )
                    else:
                        line = self.add_column(
                            line,
                            '[%s](./vc/host/%s.md) :x:' % (host['_name'], host['hash'])
                        )
                        line = self.add_column(line, '---')
                        line = self.add_column(line, '---')
                        line = self.add_column(line, '---')
                        line = self.add_column(line, '---')
                        line = self.add_column(line, '---')
                        line = self.add_column(line, '---')

                    self.my_output.print_stream(line, 'output')

    def print_readme_fi(self):
        self.my_output.print_stream(
            '\n## Fabric Interconnect\n',
            'output'
        )

        self.my_output.print_stream(
            '\nDevice | Eth | PC | Server | VMWare | OCP',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- ',
            'output'
        )

        for name in self.fi_names_hash:
            self.my_output.print_stream(
                '%s | [#%s/%s/%s](./fi/%s-eth.md) | [#%s/%s](./fi/%s-pc.md) | [#%s](./fi/%s-server.md) | [#%s](./fi/%s-vmware.md) | [#%s](./fi/%s-ocp.md)' % (
                    name,
                    self.fi_eth_up_count[name],
                    self.fi_eth_config_count[name],
                    self.fi_eth_count[name],
                    self.fi_names_hash[name],
                    self.fi_pc_up_count[name],
                    self.fi_pc_count[name],
                    self.fi_names_hash[name],
                    self.fi_server_count[name],
                    self.fi_names_hash[name],
                    self.fi_vmware_count[name],
                    self.fi_names_hash[name],
                    self.fi_ocp_count[name],
                    self.fi_names_hash[name]
                ),
                'output'
            )

    def print_readme_nexus(self):
        self.my_output.print_stream(
            '\n## Nexus\n',
            'output'
        )

        self.my_output.print_stream(
            '- %s switches [HW/SW](./nexus/devices.md) [Features](./nexus/features.md) [Mgmt](./nexus/management.md) [LLDP](./nexus/lldp.md) [CDP](./nexus/cdp.md) [Topology](./nexus/topology.md) [VPC](./nexus/vpc.md) [Eth-Up](./nexus/eth-up.md)' % (
                len(self.nexus_device_names)
            ),
            'output'
        )

        self.my_output.print_stream(
            '- %s servers with %s connected interfaces [Link](./nexus/server.md)' % (
                self.nexus_fabric_server_count,
                self.nexus_fabric_server_intf_count
            ),
            'output'
        )

        for key in self.xd_handler.vc_instance:
            self.my_output.print_stream(
                '- %s vCenter [%s] hosts with %s connected interfaces [Link](./nexus/vcenter-%s-server-fabric.md)' % (
                    self.nexus_fabric_vcenter_count[key],
                    key,
                    self.nexus_fabric_vcenter_intf_count[key],
                    key
                ),
                'output'
            )

        self.my_output.print_stream(
            '\nDevice | Conf | Eth | PC | VLAN | LLDP | CDP | MAC | Server | VMWare | OCP',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---',
            'output'
        )

        for name in self.nexus_device_names:
            self.my_output.print_stream(
                '%s | [Link](./nexus/%s-configuration.md) | [#%s/%s](./nexus/%s-eth.md) | [#%s](./nexus/%s-pc.md) | [#%s](./nexus/%s-vlan.md) | [#%s](./nexus/%s-lldp.md) | [#%s](./nexus/%s-cdp.md)| [#%s](./nexus/%s-mac.md) | [#%s](./nexus/%s-server.md) | [#%s](./nexus/%s-vmware.md) | [#%s](./nexus/%s-ocp.md)' % (
                    name,
                    name,
                    self.nexus_eth_up_count[name],
                    self.nexus_eth_count[name],
                    name,
                    self.nexus_pc_count[name],
                    name,
                    self.nexus_vlan_count[name],
                    name,
                    self.nexus_lldp_count[name],
                    name,
                    self.nexus_cdp_count[name],
                    name,
                    self.nexus_mac_count[name],
                    name,
                    self.nexus_server_count[name],
                    name,
                    self.nexus_vmware_count[name],
                    name,
                    self.nexus_ocp_count[name],
                    name
                ),
                'output'
            )

    def print_readme_cnc(self):
        self.my_output.print_stream(
            '\n## Routers (CNC)\n',
            'output'
        )

        self.my_output.print_stream(
            '\nDevice | Type | SN | IP | Software | Reach | Sync',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- | --- ',
            'output'
        )

        cnc_nodes = self.xd_handler.get_cnc_node()
        for node in cnc_nodes:
            if node['reachable']:
                reachable_tick = ':white_check_mark:'
            else:
                reachable_tick = ':x:'

            if node['sync']:
                sync_tick = ':white_check_mark:'
            else:
                sync_tick = ':x:'

            self.my_output.print_stream(
                '%s | %s | %s | %s | %s | %s | %s' % (
                    node['name'],
                    node['type'],
                    node['sn'],
                    node['ip'],
                    node['software'],
                    reachable_tick,
                    sync_tick
                ),
                'output'
            )

    def print_out_of_sync(self):
        if len(self.xd_handler.out_of_sync) == 0:
            return

        self.print_page_header('Out of sync items')
        for item in self.xd_handler.out_of_sync:
            self.my_output.print_stream(
                '- %s' % (item),
                'output'
            )

        self.save_output('out_of_sync')

    def print_readme(self):
        self.print_page_header('Vimercate Lab', main_page=True)

        self.my_output.print_stream(
            '## Inventory',
            'output'
        )
        self.my_output.print_stream(
            '- [serial numbers](./serial.md)',
            'output'
        )

        self.print_readme_server()
        self.print_readme_openshift()
        self.print_readme_vmware()
        self.print_readme_fi()
        self.print_readme_nexus()
        self.print_readme_aci()
        self.print_readme_cnc()

        self.save_output('README')

    def get_short_name(self, name):
        if name is None:
            return None

        # Re-consider
        return name

    def print(self):
        if not self.xd_handler.load_post(self.domain_name):
            print('Failed to load post XD data')
            return

        self.initialize()

        self.aci_node_mapping = self.xd_handler.get_aci_node_id2name()
        aci_nodeid2name = self.xd_handler.get_aci_node_id2name()

        self.my_output.default('Servers...')

        servers = copy.deepcopy(self.xd_handler.servers)
        macs = copy.deepcopy(self.xd_handler.servers_fabric)

        self.print_servers_details(servers)

        for tag in ['all', 'connected', 'disconnected']:
            moids = self.xd_handler.get_server_moids(tag)
            self.print_servers_list(
                servers,
                moids,
                tag
            )
            self.print_servers_fabric(
                servers,
                moids,
                tag
            )
            self.print_servers_mac(
                macs,
                moids,
                tag
            )
            self.print_aci_servers(
                servers,
                moids,
                tag
            )
            self.print_servers_nexus(
                servers,
                moids,
                tag
            )

        tags = []
        for key in self.xd_handler.vc_instance:
            tags.append(
                'vc-%s' % (key)
            )

        for key in self.xd_handler.ocp:
            tags.append(
                'ocp-%s' % (key)
            )

        for tag in tags:
            moids = self.xd_handler.get_server_moids(tag)
            self.print_servers_list(
                servers,
                moids,
                tag
            )
            self.print_servers_fabric(
                servers,
                moids,
                tag
            )
            self.print_servers_mac(
                macs,
                moids,
                tag
            )
            self.print_aci_servers(
                servers,
                moids,
                tag
            )
            self.print_servers_nexus(
                servers,
                moids,
                tag
            )

        self.print_aci(servers)
        self.print_nexus(servers)
        self.print_fi(servers)

        for key in self.xd_handler.vc_instance:
            self.print_vc(key)

        self.print_k8s()
        self.print_serial()

        self.my_output.default('Readme...')
        self.print_readme()
        self.print_out_of_sync()
