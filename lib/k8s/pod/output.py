import copy
import json


class K8sPodOutput():
    def __init__(self):
        pass

    def print_pods_state(self, info, skip=[]):
        self.my_output.my_table_ng(
            info,
            [
                ['Pod', 'namespace_nameT'],
                ['Leader', 'leaderTick'],
                ['Ready', 'container_state_summary'],
                ['Label', 'phaseT'],
                ['Annotation', 'condition.typeT'],
                ['Node', 'host_name'],
                ['IP', 'pod_ip'],
                ['Net', 'net_count'],
                ['Svc', 'svc_count'],
                ['Restart', 'container_restart_countT'],
                ['Age', 'age'],
            ],
            skip=skip
        )

    def print_pods_clusterwide_private_networks(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Pod', 'namespace_nameT'],
                ['IP', 'pod_ip'],
                ['Node', 'host_name'],
                ['Cilium', 'cilium_agent'],
                ['Private Network', 'private_network.name'],
                ['MAC', 'private_network.mac'],
                ['IPv4', 'private_network.ipv4'],
                ['IPv6', 'private_network.ipv6']
            ]
        )

    def print_pods_metadata(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Pod', 'namespace_nameT'],
                ['Owner', 'ownerT'],
                ['Label', 'labelT'],
                ['Annotation', 'annotationT']
            ]
        )


    def print_pods_container(self, info, title=False):
        new_info = []
        for item in info:
            for container_info in item['container']:
                new_item = {}
                new_item['__Output'] = {}
                new_item['namespace_nameT'] = []
                new_item['namespace_nameT'].append(
                    item['namespace']
                )
                new_item['namespace_nameT'].append(
                    item['name']
                )
                new_item['container_name'] = container_info['name']
                new_item['container_image'] = container_info['image'].split('@')
                if len(new_item['container_image']) == 2:
                    if len(new_item['container_image'][1].split(':')) == 2:
                        if new_item['container_image'][1].split(':')[0] == 'sha256':
                            new_item['container_image'][1] = '%s:...%s' % (
                                new_item['container_image'][1].split(':')[0],
                                new_item['container_image'][1].split(':')[1][-10:]
                            )

                new_item['container_command'] = container_info['command']
                new_item['container_state'] = container_info['stateT']
                new_item['__Output']['container_state'] = container_info['__Output']['stateT']
                new_item['container_restart_count'] = container_info['restart_countT']
                new_item['container_volume_count'] = len(container_info['volume_mount'])
                new_item['container_env_count'] = len(container_info['env'])
                new_item['container_cm_count'] = len(container_info['cm'])

                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'POD - Container [#%s]' % (len(new_info)),
                underline=True,
                before_newline=True
            )

        if len(new_info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_nameT',
            'container_name',
            'container_image',
            'container_command',
            'container_state',
            'container_restart_count',
            'container_volume_count',
            'container_env_count',
            'container_cm_count'
        ]

        headers = [
            'Pod',
            'Container',
            'Image',
            'Command',
            'State',
            'Restarts',
            'Vol',
            'Env',
            'CM'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['namespace_nameT', 'container_image', 'container_command']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_resource(self, info, title=False):
        if title:
            self.my_output.default(
                'POD - Resource Requirements [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            for container_info in item['container']:
                new_item = {}
                new_item['namespace_nameT'] = []
                new_item['namespace_nameT'].append(
                    item['namespace']
                )
                new_item['namespace_nameT'].append(
                    item['name']
                )
                new_item['container_name'] = container_info['name']
                new_item['requests_cpu'] = container_info['requests']['cpuT']
                new_item['requests_memory'] = container_info['requests']['memoryT']
                new_item['requests_hp'] = container_info['requests']['hpT']
                new_item['requests_custom'] = container_info['requests']['customT']
                new_item['limits_cpu'] = container_info['limits']['cpuT']
                new_item['limits_memory'] = container_info['limits']['memoryT']
                new_item['limits_hp'] = container_info['limits']['hpT']
                new_item['limits_custom'] = container_info['limits']['customT']

                new_info.append(
                    new_item
                )

        order = [
            'namespace_nameT',
            'container_name',
            'requests_cpu',
            'requests_memory',
            'requests_hp',
            'requests_custom',
            'limits_cpu',
            'limits_memory',
            'limits_hp',
            'limits_custom'
        ]

        headers = [
            'Pod',
            'Container',
            'R:CPU',
            'R:Mem',
            'R:HP',
            'R:Custom',
            'L:CPU',
            'L:Mem',
            'L:HP',
            'L:Custom'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['namespace_nameT', 'requests_custom', 'limits_custom']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_service(self, info, title=False):
        if title:
            self.my_output.default(
                'POD - Container Ports and Services (running-only) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            if item['running']:
                for container_info in item['container']:
                    new_item = {}
                    new_item['nameT'] = []
                    new_item['nameT'].append(
                        item['namespace']
                    )
                    new_item['nameT'].append(
                        item['name']
                    )
                    new_item['container'] = container_info['name']
                    new_item['port'] = container_info['port']
                    if len(new_item['port']) == 0:
                        new_item['port'].append(
                            dict(
                                portT='--',
                                hostT='--'
                            )
                        )

                    new_item['service'] = item['service']
                    if len(new_item['service']) == 0:
                        new_item['service'].append(
                            dict(
                                namespace_name='--',
                                ports='--'
                            )
                        )

                    new_info.append(
                        new_item
                    )

        order = [
            'nameT',
            'container',
            'port.portT',
            'port.hostT',
            'service.namespace_name',
            'service.ports'
        ]

        headers = [
            'Pod',
            'Container',
            'Port',
            'Host Port',
            'Service',
            'Service Ports'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['nameT', 'port', 'service']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_env(self, info, title=False):
        if title:
            self.my_output.default(
                'POD - Container Evironment Variable [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            for container_info in item['container']:
                new_item = {}
                new_item['namespace'] = item['namespace']
                new_item['name'] = item['name']
                new_item['container'] = container_info['name']
                new_item['nameT'] = []
                new_item['nameT'].append(
                    new_item['namespace']
                )
                new_item['nameT'].append(
                    new_item['name']
                )
                new_item['env'] = container_info['env']
                if len(new_item['env']) == 0:
                    new_item['env'].append(
                        dict(
                            namespace='--',
                            name='--'
                        )
                    )
                new_info.append(
                    new_item
                )

        order = [
            'nameT',
            'container',
            'env.name',
            'env.source_type',
            'env.source_value'
        ]

        headers = [
            'Pod',
            'Container',
            'Env',
            'Source',
            'Value'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['nameT', 'env']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_cm(self, info, title=False):
        if title:
            self.my_output.default(
                'POD - Container Config Map [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            for container_info in item['container']:
                new_item = {}
                new_item['namespace'] = item['namespace']
                new_item['name'] = item['name']
                new_item['nameT'] = []
                new_item['nameT'].append(
                    new_item['namespace']
                )
                new_item['nameT'].append(
                    new_item['name']
                )
                new_item['container'] = container_info['name']
                new_item['cm'] = container_info['cm']
                if len(new_item['cm']) == 0:
                    new_item['cm'].append(
                        dict(
                            namespace='--',
                            name='--'
                        )
                    )
                new_info.append(
                    new_item
                )

        order = [
            'nameT',
            'container',
            'cm.namespace',
            'cm.name'
        ]

        headers = [
            'Pod',
            'Container',
            'CM Namespace',
            'CM Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['nameT', 'cm']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_vol(self, info, title=False):
        new_info = []
        for item in info:
            for container_info in item['container']:
                new_item = {}
                new_item['nameT'] = []
                new_item['nameT'].append(
                    item['namespace']
                )
                new_item['nameT'].append(
                    item['name']
                )
                new_item['container'] = container_info['name']
                new_item['volume_mount'] = []

                for volume_mount in container_info['volume_mount']:
                    volume_mount['source'] = ''

                    if volume_mount['type'] == 'host_path':
                        if volume_mount['read_only'] is None or not volume_mount['read_only']:
                            volume_mount['path'] = '(ro) %s' % (volume_mount['path'])
                        else:
                            volume_mount['path'] = '(rw) %s' % (volume_mount['path'])

                        volume_mount['source'] = volume_mount['mo']['path']
                        if volume_mount['sub_path'] is not None:
                            volume_mount['source'] = '%s/%s' % (
                                volume_mount['source'],
                                volume_mount['sub_path']
                            )
                        new_item['volume_mount'].append(
                            volume_mount
                        )
                        continue

                    if volume_mount['type'] == 'config_map':
                        if volume_mount['mo']['items'] is None:
                            volume_mount['source'] = volume_mount['mo']['name']
                            new_item['volume_mount'].append(
                                volume_mount
                            )
                            continue

                        for item_mo in volume_mount['mo']['items']:
                            new_volume_mount = copy.deepcopy(volume_mount)
                            new_volume_mount['source'] = '%s:%s' % (
                                volume_mount['mo']['name'],
                                item_mo['key']
                            )
                            new_volume_mount['path'] = '%s/%s' % (
                                volume_mount['path'],
                                item_mo['path']
                            )
                            new_item['volume_mount'].append(
                                new_volume_mount
                            )

                        continue

                    if volume_mount['type'] == 'secret':
                        if volume_mount['mo']['items'] is None:
                            volume_mount['source'] = volume_mount['mo']['secret_name']
                            new_item['volume_mount'].append(
                                volume_mount
                            )
                            continue

                        for item_mo in volume_mount['mo']['items']:
                            new_volume_mount = copy.deepcopy(volume_mount)
                            new_volume_mount['source'] = '%s:%s' % (
                                volume_mount['mo']['secret_name'],
                                item_mo['key']
                            )
                            new_volume_mount['path'] = '%s/%s' % (
                                volume_mount['path'],
                                item_mo['path']
                            )
                            new_item['volume_mount'].append(
                                new_volume_mount
                            )

                        continue

                    if volume_mount['type'] == 'downward_api':
                        if volume_mount['mo']['items'] is not None:
                            for item_mo in volume_mount['mo']['items']:
                                new_volume_mount = copy.deepcopy(volume_mount)
                                if item_mo['field_ref'] is not None:
                                    new_volume_mount['source'] = item_mo['field_ref']['field_path']
                                    new_volume_mount['path'] = '%s/%s' % (
                                        volume_mount['path'],
                                        item_mo['path']
                                    )
                                    new_item['volume_mount'].append(
                                        new_volume_mount
                                    )

                            continue

                    if volume_mount['type'] == 'projected':
                        for projected_mo in volume_mount['mo']:
                            if projected_mo['type'] == 'config_map':
                                volume_mount['type'] = 'config_map (p)'
                                if projected_mo['mo']['items'] is None:
                                    volume_mount['source'] = projected_mo['mo']['name']
                                    new_item['volume_mount'].append(
                                        projected_mo
                                    )
                                    continue

                                for item_mo in projected_mo['mo']['items']:
                                    new_volume_mount = copy.deepcopy(volume_mount)
                                    new_volume_mount['source'] = '%s:%s' % (
                                        projected_mo['mo']['name'],
                                        item_mo['key']
                                    )
                                    new_volume_mount['path'] = '%s/%s' % (
                                        volume_mount['path'],
                                        item_mo['path']
                                    )
                                    new_item['volume_mount'].append(
                                        new_volume_mount
                                    )

                            if projected_mo['type'] == 'secret':
                                volume_mount['type'] = 'secret (p)'
                                if projected_mo['mo']['items'] is None:
                                    volume_mount['source'] = projected_mo['mo']['name']
                                    new_item['volume_mount'].append(
                                        volume_mount
                                    )
                                    continue

                                for item_mo in projected_mo['mo']['items']:
                                    new_volume_mount = copy.deepcopy(volume_mount)
                                    new_volume_mount['source'] = '%s:%s' % (
                                        projected_mo['mo']['name'],
                                        item_mo['key']
                                    )
                                    new_volume_mount['path'] = '%s/%s' % (
                                        volume_mount['path'],
                                        item_mo['path']
                                    )
                                    new_item['volume_mount'].append(
                                        new_volume_mount
                                    )

                            if projected_mo['type'] == 'downward_api':
                                volume_mount['type'] = 'downward_api (p)'
                                if projected_mo['mo']['items'] is not None:
                                    for item_mo in projected_mo['mo']['items']:
                                        new_volume_mount = copy.deepcopy(volume_mount)
                                        if item_mo['field_ref'] is not None:
                                            new_volume_mount['source'] = item_mo['field_ref']['field_path']
                                            new_volume_mount['path'] = '%s/%s' % (
                                                volume_mount['path'],
                                                item_mo['path']
                                            )
                                            new_item['volume_mount'].append(
                                                new_volume_mount
                                            )

                                    continue

                            if projected_mo['type'] == 'service_account_token':
                                volume_mount['type'] = 'service_account_token (p)'
                                new_volume_mount = copy.deepcopy(volume_mount)
                                new_volume_mount['path'] = '%s/%s' % (
                                    volume_mount['path'],
                                    projected_mo['mo']['path']
                                )
                                new_item['volume_mount'].append(
                                    new_volume_mount
                                )
                                continue

                        continue

                    new_item['volume_mount'].append(
                        volume_mount
                    )

                new_info.append(
                    new_item
                )

        if title:
            self.my_output.default(
                'POD - Container Volume Mount [#%s]' % (len(new_info)),
                underline=True,
                before_newline=True
            )

        if len(new_info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameT',
            'container',
            'volume_mount.type',
            'volume_mount.source',
            'volume_mount.path'
        ]

        headers = [
            'Pod',
            'Container',
            'Volume Type',
            'Volume Source',
            'Mount Path'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['nameT', 'volume_mount']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_net(self, info, title=False):
        if title:
            self.my_output.default(
                'POD - Networking [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            new_item = {}
            new_item['__Output'] = {}
            new_item['nameT'] = []
            new_item['nameT'].append(
                item['namespace']
            )
            new_item['nameT'].append(
                item['name']
            )
            new_item['container_state_summary'] = item['container_state_summary']
            new_item['phaseT'] = item['phaseT']
            new_item['__Output']['phaseT'] = item['__Output']['phaseT']

            if item['host_network']:
                new_item['host_network_tick'] = '\u2713'
            else:
                new_item['host_network_tick'] = '\u2717'

            new_item['network'] = item['network']
            for network_info in new_item['network']:
                if network_info['mac'] is None:
                    network_info['mac'] = '--'

                network_info['ip'] = ','.join(
                    network_info['ips']
                )

                if len(network_info['dns']) > 0:
                    network_info['dnsT'] = json.dumps(network_info['dns'])
                else:
                    network_info['dnsT'] = '--'

                if network_info['pci'] is None:
                    network_info['pciT'] = '--'
                else:
                    network_info['pciT'] = network_info['pci']

                if network_info['default']:
                    network_info['default'] = '\u2713'
                else:
                    network_info['default'] = '\u2717'

            new_info.append(
                new_item
            )

        order = [
            'nameT',
            'host_network_tick',
            'network.interface',
            'network.name',
            'network.default',
            'network.mac',
            'network.ip',
            'network.dnsT',
            'network.pciT'
        ]

        headers = [
            'Pod',
            'HostNet',
            'Intf',
            'Network',
            'Def',
            'MAC',
            'IP',
            'DNS',
            'PCI'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['nameT', 'network']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pods_log(self, info, title=False):
        for item in info:
            for container_name in item['log']:
                if title:
                    self.my_output.default(
                        'POD Log - %s/%s/%s' % (item['namespace'], item['name'], container_name),
                        underline=True,
                        before_newline=True
                    )

                if item['log'][container_name] is None or len(item['log'][container_name]) == 0:
                    self.my_output.default('None')
                    return

                self.my_output.default('')
                self.my_output.default(item['log'][container_name], wrap='~~~')
