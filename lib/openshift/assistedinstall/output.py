import json
from lib import file_helper


class AssistedInstallOutput():
    def __init__(self):
        pass

    def print_assisted_install_clusters_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Assisted Installation - Clusters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'status_info',
            'openshift_version',
            'network_type'
        ]

        headers = [
            'Name',
            'Status',
            'Version',
            'CNI'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_assisted_install_cluster_cidr(self, cluster):
        if 'cidr' not in cluster or cluster['cidr'] is None:
            self.my_output.default('[WARNING] CIDR information not found')
            return

        order = [
            'type',
            'cidr',
            'prefix'
        ]

        headers = [
            'Type',
            'Subnet',
            'Prefix'
        ]

        for cidr in cluster['cidr']:
            if cidr['prefix'] is None:
                cidr['prefix'] = '--'

        self.my_output.my_table(
            cluster['cidr'],
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_assisted_install_cluster_config(self, cluster):
        if 'config' not in cluster or cluster['config'] is None:
            self.my_output.default('[WARNING] Configuration information not found')
            return

        self.my_output.default(
            'Cluster configuration',
            underline=True,
            after_newline=True,
            before_newline=True
        )

        self.my_output.default(json.dumps(cluster['config'], indent=4))

    def print_assisted_install_cluster_static_network_config(self, cluster):
        if 'static_network_config' not in cluster or cluster['static_network_config'] is None:
            return

        if len(cluster['static_network_config']) == 0:
            return

        index = 1
        for config in cluster['static_network_config']:
            self.my_output.default(
                'Static network configuration #%s' % (index),
                underline=True,
                after_newline=True,
                before_newline=True
            )

            self.my_output.default(
                config['network_yaml']
            )

            order = [
                'logical_nic_name',
                'mac_address'
            ]

            headers = [
                'Logical nic name',
                'MAC address'
            ]

            self.my_output.my_table(
                config['mac_interface_map'],
                order=order,
                headers=headers,
                row_separator=True,
                allow_order_subkeys=True,
                underline=True,
                table=True
            )

            index = index + 1

    def print_assisted_install_cluster_hosts(self, cluster):
        if 'hosts' not in cluster or cluster['hosts'] is None or len(cluster['hosts']) == 0:
            self.my_output.default('[WARNING] No discovered hosts information')
            return

        self.my_output.default(
            'Hosts discovery',
            underline=True,
            before_newline=True
        )

        order = [
            'hostname',
            'suggested_role',
            'role',
            'inventory.bmc_address',
            'status_info',
            'ntp_ready_tick',
            'is_valid.hardware_tick',
            'is_valid.network_tick',
            'is_valid.operators_tick',
            'updated_at'
        ]

        headers = [
            'Hostname',
            'Suggested Role',
            'Role',
            'IMC',
            'Status',
            'NTP Ready',
            'HW Valid',
            'Network Valid',
            'Operator Valid',
            'Updated'
        ]

        self.my_output.my_table(
            cluster['hosts'],
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

        for host_info in cluster['hosts']:
            if 'inventory' not in host_info or host_info['inventory'] is None:
                self.my_output.default('[WARNING] No inventory info')
            else:
                order = [
                    'inventory.bmc_address',
                    'inventory.bmc_v6address',
                    'inventory.hostname',
                    'id',
                    'infra_env_id',
                    'inventory.system_vendor.manufacturer',
                    'inventory.system_vendor.product_name',
                    'inventory.system_vendor.serial_number',
                    'inventory.boot.command_line',
                    'inventory.boot.current_boot_mode',
                    'inventory.cpu.architecture',
                    'inventory.cpu.count',
                    'inventory.cpu.frequency',
                    'inventory.cpu.model_name',
                    'inventory.memory.physical_bytes',
                    'inventory.memory.usable_bytes'
                ]

                headers = [
                    'IMC v4',
                    'IMC v6',
                    'Hostname',
                    'Id',
                    'Infra Id',
                    'Vendor',
                    'Product',
                    'Serial',
                    'Boot cmd',
                    'Boot mode',
                    'CPU architecture',
                    'CPU count',
                    'CPU frequency',
                    'CPU model',
                    'Memory physical bytes',
                    'Memory usable bytes'
                ]

                self.my_output.dictionary(
                    host_info,
                    title='Host %s' % (host_info['inventory']['bmc_address']),
                    keys=order,
                    title_keys=headers,
                    justify=True
                )

                if 'interfaces' not in host_info['inventory'] or host_info['inventory']['interfaces'] is None:
                    self.my_output.default('[WARNING] No interfaces info')
                else:
                    order = [
                        'name',
                        'biosdevname',
                        'type',
                        'mac_address',
                        'mtu',
                        'ipv4_addresses',
                        'ipv6_addresses',
                        'has_carrier',
                        'flags'
                    ]

                    headers = [
                        'Inteface Name',
                        'Bios name',
                        'Type',
                        'MAC',
                        'MTU',
                        'IPv4',
                        'IPv6',
                        'Carrier',
                        'Flags'
                    ]

                    self.my_output.my_table(
                        self.my_output.expand_lists(
                            host_info['inventory']['interfaces'],
                            order,
                            ['ipv4_addresses', 'ipv6_addresses', 'flags']
                        ),
                        order=order,
                        headers=headers,
                        row_separator=True,
                        allow_order_subkeys=True,
                        underline=True,
                        table=True
                    )

                if 'routes' not in host_info['inventory'] or host_info['inventory']['routes'] is None:
                    self.my_output.default('[WARNING] No disks info')
                else:
                    order = [
                        'destination',
                        'gateway',
                        'interface'
                    ]

                    headers = [
                        'Route',
                        'Gateway',
                        'Interface'
                    ]

                    self.my_output.my_table(
                        host_info['inventory']['routes'],
                        order=order,
                        headers=headers,
                        row_separator=True,
                        allow_order_subkeys=True,
                        underline=True,
                        table=True
                    )

                if 'disks' not in host_info['inventory'] or host_info['inventory']['disks'] is None:
                    self.my_output.default('[WARNING] No disks info')
                else:
                    order = [
                        'name',
                        'path',
                        'size_bytes',
                        'drive_type',
                        'bootable',
                        'target_tick',
                        'vendor',
                        'model'
                    ]

                    headers = [
                        'Disk name',
                        'Path',
                        'Size [B]',
                        'Type',
                        'Bootable',
                        'Target',
                        'Vendor',
                        'Model'
                    ]

                    disks = []
                    for disk_info in host_info['inventory']['disks']:
                        if disk_info['installation_eligibility']['not_eligible_reasons'] is None:
                            disks.append(
                                disk_info
                            )

                    self.my_output.my_table(
                        disks,
                        order=order,
                        headers=headers,
                        row_separator=True,
                        allow_order_subkeys=True,
                        underline=True,
                        table=True
                    )

            if 'ntp_sources' not in host_info or host_info['ntp_sources'] is None:
                self.my_output.default('[WARNING] No NTP sources info')
            else:
                order = [
                    'source_name',
                    'reachable_tick'
                ]

                headers = [
                    'NTP Source',
                    'Reachable'
                ]

                self.my_output.my_table(
                    host_info['ntp_sources'],
                    order=order,
                    headers=headers,
                    row_separator=True,
                    allow_order_subkeys=True,
                    underline=True,
                    table=True
                )

            if 'validations_info' not in host_info or host_info['validations_info'] is None:
                self.my_output.default('[WARNING] No validation info')
            else:
                order = [
                    'type',
                    'id',
                    'status',
                    'message'
                ]

                headers = [
                    'Validation type',
                    'Id',
                    'Status',
                    'Message'
                ]

                self.my_output.my_table(
                    host_info['validations_info'],
                    order=order,
                    headers=headers,
                    row_separator=True,
                    allow_order_subkeys=True,
                    underline=True,
                    table=True
                )

    def print_assisted_install_cluster_kubeconfig(self, cluster):
        if 'kubeconfig' in cluster and cluster['kubeconfig'] is not None:
            content = file_helper.get_file_text(
                cluster['kubeconfig']
            )
            self.my_output.default(
                'Kubeconfig',
                underline=True,
                before_newline=True,
                after_newline=True
            )
            self.my_output.default(content)

    def print_assisted_install_cluster_credentials(self, cluster):
        order = [
            'credentials.console_url',
            'credentials.username',
            'credentials.password'
        ]

        headers = [
            'URL',
            'Username',
            'Password'
        ]

        self.my_output.dictionary(
            cluster,
            title='Cluster console access',
            values=cluster,
            keys=order,
            title_keys=headers,
            justify=True
        )

    def print_assisted_install_cluster(self, cluster):
        order = [
            'name',
            'id',
            'user_name',
            'platform.type',
            'openshift_version',
            'ocp_release_image',
            'network_type',
            'high_availability_mode',
            'status_info',
            'created_at',
            'base_dns_domain',
            'api_vipsT',
            'ingress_vipsT',
            'http_proxy',
            'https_proxy',
            'no_proxy',
            'ssh_public_key',
            'iso_type',
            'iso_url',
            'credentials.console_url',
            'credentials.username',
            'credentials.password'
        ]

        headers = [
            'Name',
            'Id',
            'Owner',
            'Type',
            'Version',
            'Image',
            'CNI',
            'HA Mode',
            'Status',
            'Created at',
            'Base DNS',
            'API VIP',
            'Ingress VIP',
            'HTTP proxy',
            'HTTPS proxy',
            'No proxy',
            'SSH public key',
            'ISO Type',
            'ISO URL',
            'Console URL',
            'Username',
            'Password'
        ]

        cluster['api_vipsT'] = '--'
        if 'api_vips' in cluster and cluster['api_vips'] is not None:
            api_vips = []
            for api_vip in cluster['api_vips']:
                api_vips.append(
                    api_vip['ip']
                )

            cluster['api_vipsT'] = ', '.join(api_vips)

        cluster['ingress_vipsT'] = '--'
        if 'ingress_vips' in cluster and cluster['ingress_vips'] is not None:
            ingress_vips = []
            for ingress_vip in cluster['ingress_vips']:
                ingress_vips.append(
                    ingress_vip['ip']
                )

            cluster['ingress_vipsT'] = ', '.join(ingress_vips)

        self.my_output.dictionary(
            cluster,
            title='Assisted Installation - Cluster [%s]' % (cluster['name']),
            values=cluster,
            keys=order,
            title_keys=headers,
            justify=True
        )

        self.print_assisted_install_cluster_cidr(cluster)
        self.print_assisted_install_cluster_config(cluster)
        self.print_assisted_install_cluster_static_network_config(cluster)
        self.print_assisted_install_cluster_hosts(cluster)
        self.print_assisted_install_cluster_kubeconfig(cluster)

    def print_assisted_install_versions(self, info, title=False):
        if title:
            self.my_output.default(
                'Assisted Installation - OpenShift version [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'display_name',
            'support_level',
            'cpu_architectures'
        ]

        headers = [
            'Name',
            'Support',
            'CPU'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
