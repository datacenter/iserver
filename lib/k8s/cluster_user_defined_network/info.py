class K8sClusterUserDefinedNetworkInfo():
    def __init__(self):
        self.cluster_user_defined_network = None

    def get_cluster_user_defined_network_info(self, managed_object):
        condition_map = {}
        condition_map['created'] = 'NetworkCreated'

        info = self.get_base_info(
            managed_object,
            condition_map=condition_map
        )

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['reasonT'] = []
        if not info['created'] and info['created_status'] is not None:
            info['reasonT'].append(
                '[%s] %s' % (
                    info['created_reason'],
                    info['created_message']
                )
            )

        info['topology'] = self.get(managed_object, 'spec:network:topology')
        info['role'] = None
        info['subnet'] = []
        info['subnetT'] = []

        if info['topology'] == 'Layer2':
            info['role'] = self.get(managed_object, 'spec:network:layer2:role')
            info['subnet'] = self.get(managed_object, 'spec:network:layer2:subnets', on_error=[], on_none=[])
            info['subnetT'] = info['subnet']

        if info['topology'] == 'Layer3':
            info['role'] = self.get(managed_object, 'spec:network:layer3:role')
            info['subnet'] = self.get(managed_object, 'spec:network:layer3:subnets', on_error=[], on_none=[])
            info['subnetT'] = []
            for item in info['subnet']:
                info['subnetT'].append(
                    item['cidr']
                )
                info['subnetT'].append(
                    'host /%s' % (
                        item['hostSubnet']
                    )
                )

        info['primary'] = False
        info['primaryTick'] = ''
        if info['role'] == 'Primary':
            info['primary'] = True
            info['primaryTick'] = '\u2713'
            info['__Output']['primaryTick'] = 'Green'

        return info

    def add_cluster_user_defined_networks_info(self, infos, nad_info=False, usage_info=False, cache_enabled=True):
        if nad_info:
            for item in infos:
                item['namespace'] = []
                item['nad'] = None

            nads = self.get_nads(cache_enabled=cache_enabled)
            if nads is not None:
                for nad in nads:
                    for item in infos:
                        if item['name'] == nad['cudn']:
                            item['namespace'].append(nad['namespace'])
                            item['nad'] = nad['config']
                            item['nad']['netAttachDefName'] = '${NAMESPACE}/%s' % (nad['name'])


        pods_namespace = {}
        vms_namespace = {}
        if usage_info:
            for item in infos:
                item['pod'] = []
                item['vm'] = []
                item['app'] = []

                for namespace in item['namespace']:
                    if namespace not in pods_namespace:
                        pods_namespace[namespace] = self.get_pods(
                            namespace=namespace, 
                            cache_enabled=cache_enabled
                        )
                        if pods_namespace[namespace] is None:
                            pods_namespace[namespace] = []

                    if namespace not in vms_namespace:
                        vms_namespace[namespace] = self.get_virtual_machine_instances(
                            object_filter=['namespace:%s' % (namespace)],
                            cache_enabled=cache_enabled
                        )
                        if vms_namespace[namespace] is None:
                            vms_namespace[namespace] = []
            
            for item in infos:
                for namespace in item['namespace']:
                    if item['primary']:
                        for pod in pods_namespace[namespace]:
                            if self.is_pod_virt_launcher(pod):
                                continue

                            for network in pod['network']:
                                if network['default']:
                                    item['pod'].append('%s/%s' % (pod['namespace'], pod['name']))
                                    item['app'].append('[POD] %s/%s (%s)' % (pod['namespace'], pod['name'], network['interface']))

                        for vmi in vms_namespace[namespace]:
                            for interface in vmi['interface']:
                                if self.get(interface, 'network:type') == 'pod':
                                    if self.get(interface, 'network:info') == 'pod:l2bridge':
                                        item['vm'].append('%s/%s' % (vmi['namespace'], vmi['name']))
                                        item['app'].append('[VM] %s/%s (%s)' % (vmi['namespace'], vmi['name'], self.get(interface, 'device:name')))

                    if not item['primary']:
                        for pod in pods_namespace[namespace]:
                            if not self.is_pod_virt_launcher(pod):
                                for network in pod['network']:
                                    if network['name'] == '%s/%s' % (namespace, item['name']):
                                        item['pod'].append('%s/%s' % (pod['namespace'], pod['name']))
                                        item['app'].append('[POD] %s/%s (%s)' % (pod['namespace'], pod['name'], network['interface']))

                        for vmi in vms_namespace[namespace]:
                            for interface in vmi['interface']:
                                if self.get(interface, 'network:type') == 'multus':
                                    if self.get(interface, 'network:multus:networkName') == '%s/%s' % (namespace, item['name']):
                                        item['vm'].append('%s/%s' % (vmi['namespace'], vmi['name']))
                                        item['app'].append('[VM] %s/%s (%s)' % (vmi['namespace'], vmi['name'], self.get(interface, 'device:name')))

        return infos

    def get_cluster_user_defined_networks(self, object_filter=None, nad_info=False, usage_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cluster_user_defined_network', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if return_mo:
            return infos

        if infos is not None:
            infos = self.add_cluster_user_defined_networks_info(
                infos,
                nad_info=nad_info,
                usage_info=usage_info
            )

        return infos
    
    def is_cluster_user_defined_network(self, name, cache_enabled=True):
        if self.get_cluster_user_defined_network(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cluster_user_defined_network(self, name, nad_info=False, usage_info=False, return_mo=False, cache_enabled=True):
        return self.get_info(
            'cluster_user_defined_network', 
            name,
            nad_info=nad_info,
            usage_info=usage_info,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
    