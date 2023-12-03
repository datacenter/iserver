class OcpVmOutput():
    def __init__(self):
        pass

    def print_ocp_vm_base_info(self, info, stream='default'):
        order = [
            'namespace',
            'name',
            'node_name',
            'cpu.cores',
            'memory',
            'state',
            'readyTick',
            'failureTick',
            'liveMigrationTick',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Node',
            'CPU',
            'Memory',
            'State',
            'Ready',
            'Failure',
            'LM',
            'Age'
        ]

        self.my_output.dictionary(
            info,
            title='OCP Virtual Machine',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers,
            stream=stream
        )

    def print_ocp_vm_info(self, info, stream='default'):
        self.print_ocp_vm_base_info(info, stream=stream)

        if len(info['failures']) > 0:
            for failure in info['failures']:
                self.my_output.default(
                    'Failure: %s' % (failure['reason']),
                    before_newline=True
                )
                self.my_output.default(
                    failure['message']
                )

    def print_ocp_vm_disks_info(self, info, show_vm_info=True, stream='default'):
        if show_vm_info:
            self.print_ocp_vm_base_info(info, stream=stream)

        order = [
            'name',
            'type',
            'bus',
            'target',
            'volume.type',
            'persistent_volume_claim_info.name',
            'persistent_volume_claim_info.phase',
            'persistent_volume_claim_info.storage_class_name',
            'persistent_volume_claim_info.access_modes_string',
            'persistent_volume_claim_info.capacity.storage',
            'persistent_volume_claim_info.volume_mode'
        ]

        headers = [
            'Name',
            'Type',
            'Bus',
            'Target',
            'Volume Type',
            'Volume Name',
            'Volume State',
            'SC',
            'Access Modes',
            'Storage',
            'Volume Mode'
        ]

        self.my_output.my_table(
            info['disks'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            stream=stream
        )

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

    def print_ocp_vm_pod_info(self, info, show_vm_info=True):
        if show_vm_info:
            self.print_ocp_vm_base_info(info)

    def print_deployment_service_access_info(self, info):
        order = [
            'namespace',
            'name',
            'ip',
            'port',
            'auth'
        ]

        headers = [
            'Service Namespace',
            'Service Name',
            'Node IP',
            'Node Port',
            'Authentication Info'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            table=True
        )

    def print_ocp_vms(self, info, title=False):
        if title:
            self.my_output.default(
                'OCP VM [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'node_name',
            'cpu.cores',
            'memory',
            'disks.info',
            'interfaces.info',
            'state',
            'readyTick',
            'failures',
            'services.namespace_name',
            'services.ports',
            'liveMigrationTick',
            'age'
        ]

        headers = [
            'VM',
            'Node',
            'CPU',
            'Memory',
            'Disks',
            'Interfaces',
            'State',
            'Ready',
            'Failure',
            'Service',
            'NodePort',
            'LM',
            'Age'
        ]

        for item in info:
            if len(item['failures']) == 0:
                item['failures'].append('--')

            if len(item['services']) == 0:
                item['services'].append(
                    dict(
                        namespace_name='--',
                        ports='--'
                    )
                )

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disks', 'interfaces', 'services', 'failures']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            table=True
        )

    def print_ocp_vms_intf(self, info, title=False):
        if title:
            self.my_output.default('Kubernetes Networking', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'interfaces.name',
            'interfaces.mac_address',
            'interfaces.ip_address',
            'interfaces.masqueradeTick',
            'interfaces.podTick',
            'interfaces.sriovTick',
            'interfaces.multusTick',
            'interfaces.multusNetworkName',
            'interfaces.vlan',
            'interfaces.resourceName',
            'interfaces.policyName',
            'interfaces.sriovDeviceType',
            'interfaces.sriovNic'
        ]

        headers = [
            'VM',
            'Interface',
            'MAC',
            'IP',
            'Masq',
            'Pod',
            'SRIOV',
            'Multus',
            'Network',
            'VLAN Tag',
            'Resource',
            'Policy',
            'Device Type',
            'NIC'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interfaces']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_sriov(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Host Networking', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'interfaces.name',
            'interfaces.hostIf.name',
            'interfaces.hostIf.numa',
            'interfaces.hostIf.index',
            'interfaces.hostIf.flags',
            'interfaces.hostIf.mtu',
            'interfaces.hostIf.state',
            'interfaces.hostIf.mac',
            'interfaces.hostIf.vf.index',
            'interfaces.hostIf.vf.vlan',
            'interfaces.hostIf.vf.spoof',
            'interfaces.hostIf.vf.link',
            'interfaces.hostIf.vf.trust'
        ]

        headers = [
            'VM',
            'VM Interface',
            'Host Interface',
            'Numa',
            'ifIndex',
            'Flags',
            'MTU',
            'State',
            'MAC',
            'VF Index',
            'VF VLAN',
            'VF Spoof',
            'VF Link',
            'VF Trust'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interfaces'],
                filtering_rules=[
                    'sriovEnabled:bool:false'
                ],
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_fabric(self, info, title=False):
        if title:
            self.my_output.default('SR-IOV Fabric Connectivity', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'fabric.name',
            'fabric.type_controller',
            'fabric.mac',
            'fabric.encap',
            'fabric.vrf',
            'fabric.ips',
            'fabric.interfaces'
        ]

        headers = [
            'VM',
            'VM Interface',
            'Fabric',
            'MAC',
            'Encapsulation',
            'VRF',
            'IP Address',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fabric']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_bgp(self, info, title=False):
        if title:
            self.my_output.default('BGP Sessions', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'bgp.name',
            'bgp.type_controller',
            'bgp.pod_node_name',
            'bgp.bgpDomainName',
            'bgp.asn',
            'bgp.addr',
            'bgp.nbrType',
            'bgp.state',
            'bgp.paths'
        ]

        headers = [
            'VM',
            'VM Interface',
            'Fabric',
            'Node',
            'VRF',
            'ASN',
            'Address',
            'Type',
            'State',
            'Paths (AF IPv4)'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['bgp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_service(self, info, title=False):
        if title:
            self.my_output.default('Kubernetes Services', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'services.specialT',
            'services.namespace_name',
            'services.type',
            'services.cluster_ip',
            'services.external_traffic_policy',
            'services.ports',
            'services.age'
        ]

        headers = [
            'VM',
            'Selector',
            'Service',
            'Type',
            'Cluster IP',
            'External Traffic Policy',
            'Port',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['services']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_disk(self, info, title=False):
        if title:
            self.my_output.default('Disks', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'disks.name',
            'disks.type',
            'disks.bus',
            'disks.volume.type',
            'disks.volume.name',
            'disks.persistent_volume_claim_info.capacity.storage',
            'disks.pvc_name',
            'disks.persistent_volume_claim_info.access_modes',
            'disks.persistent_volume_claim_info.volume_mode',
            'disks.storage_class_name',
            'disks.pod_name'
        ]

        headers = [
            'VM',
            'Disk Name',
            'Type',
            'Bus',
            'Volume Type',
            'Volume',
            'Size',
            'PVC',
            'PVC Access',
            'PVC Mode',
            'Storage Class',
            'POD'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disks']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )

    def print_ocp_vms_csi(self, info, title=False):
        if title:
            self.my_output.default('CSI', underline=True, before_newline=True)

        order = [
            'namespace_name',
            'disks.name',
            'disks.type',
            'disks.pv.csi_driver',
            'disks.lvm.path',
            'disks.lvm.vg',
            'disks.lvm.access',
            'disks.lvm.pool',
            'disks.lvm.status',
            'disks.lvm.size',
            'disks.lvm.mapped'
        ]

        headers = [
            'VM',
            'Disk Name',
            'Type',
            'CSI Driver',
            'LVM Path',
            'VG Name',
            'LV Write Access',
            'LV Pool',
            'LV Status',
            'LV Size',
            'Mapped Size'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disks']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            cast_none=True,
            table=True
        )
