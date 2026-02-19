import copy
from lib import filter_helper
from lib import ip_helper


class K8sServiceInfo():
    def __init__(self):
        self.service = None

    def get_service_info(self, service_mo):
        if service_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            service_mo
        )
        info.update(metadata_info)

        # ExternalName, ClusterIP, NodePort, and LoadBalancer
        info['type'] = self.get(service_mo, 'spec:type')

        info['cluster_ip'] = self.get(service_mo, 'spec:cluster_ip', on_error=None)
        if info['cluster_ip'] == 'None':
            info['cluster_ip'] = None

        info['cluster_ips'] = self.get(service_mo, 'spec:cluster_i_ps', on_error=[], on_none=[])
        if len(info['cluster_ips']) == 1 and 'None' in info['cluster_ips']:
            info['cluster_ips'] = []

        info['external_traffic_policy'] = self.get(service_mo, 'spec:external_traffic_policy')

        info['external_ips'] = self.get(service_mo, 'spec:external_i_ps', on_error=[], on_none=[])
        if len(info['external_ips']) == 1 and 'None' in info['external_ips']:
            info['external_ips'] = []

        info['external_name'] = self.get(service_mo, 'spec:external_name')
        info['load_balancer_ip'] = self.get(service_mo, 'spec:load_balancer_ip')
        info['load_balancer_ingress'] = self.get(service_mo, 'status:load_balancer:ingress')

        info['ipT'] = []
        if info['type'] == 'ExternalName':
            info['cluster_ipT'] = ['--']
            info['external_ipT'] = [info['external_name']]
            info['ipT'].append(
                info['external_name']
            )
        if info['type'] in ['ClusterIP', 'NodePort', 'LoadBalancer']:
            info['cluster_ipT'] = info['cluster_ips']
            info['external_ipT'] = info['external_ips']
            info['ipT'] = info['ipT'] + info['cluster_ips'] + info['external_ips']

        info['portT'] = []
        info['port'] = []
        ports_mo = self.get(service_mo, 'spec:ports', on_error=[], on_none=[])
        for port_mo in ports_mo:
            service_keys = [
                'app_protocol',
                'name',
                'node_port',
                'port',
                'protocol',
                'target_port'
            ]
            port_info = {}

            for service_key in service_keys:
                port_info[service_key] = self.get(port_mo, service_key)

            port_info['descr'] = '--'

            if info['type'] in ['NodePort', 'LoadBalancer']:
                port_info['descr'] = '%s/%s:%s' % (
                    port_info['protocol'],
                    port_info['port'],
                    port_info['node_port']
                )
                if port_info['name'] is not None:
                    port_info['descr'] = '%s [%s]' % (
                        port_info['descr'],
                        port_info['name']
                    )

            if info['type'] == 'ClusterIP':
                port_info['descr'] = '%s/%s' % (
                    port_info['protocol'],
                    port_info['port']
                )
                if port_info['name'] is not None:
                    port_info['descr'] = '%s [%s]' % (
                        port_info['descr'],
                        port_info['name']
                    )
                    
            info['portT'].append(
                port_info['descr']
            )
            info['port'].append(
                port_info
            )

        info['portT'] = sorted(info['portT'])
        info['ports'] = ','.join(info['portT'])

        info['special'] = None
        info['specialT'] = '--'

        info['selector'] = self.get(service_mo, 'spec:selector', on_error={}, on_none={})
        info['selectorT'] = []

        for key in info['selector']:
            info['selectorT'].append(
                '%s:%s' % (
                    key,
                    info['selector'][key]
                )
            )
            if key == 'special':
                info['special'] = info['selector'][key]
                info['specialT'] = info['selector'][key]

        return info

    def get_services_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service is not None:
                return self.service

        managed_objects = self.get_service_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service = []
        for managed_object in managed_objects:
            service_info = {}
            service_info['info'] = self.get_service_info(
                managed_object
            )
            service_info['mo'] = managed_object
            self.service.append(
                service_info
            )

        return self.service

    def match_service(self, service_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (service_info['namespace'], service_info['name'])):
                    return False

            if key == 'owner':
                key_found = True
                if not filter_helper.match_namespace_name(value, service_info['owner']):
                    return False

            if key == 'type':
                key_found = True
                if not filter_helper.match_string(value, service_info['type']):
                    return False

            if key == 'cluster-ip':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if cluster_ip == value:
                        value_match = True

                if not value_match:
                    return False

            if key == 'cluster-subnet':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if ip_helper.is_ipv4_in_cidr(cluster_ip, value):
                        value_match = True

                if not value_match:
                    return False

            if key == 'cluster-string':
                key_found = True
                value_match = False
                for cluster_ip in service_info['cluster_ips']:
                    if filter_helper.match_string(cluster_ip, value):
                        value_match = True

            if key == 'external-ip':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if external_ip == value:
                        value_match = True

                if not value_match:
                    return False

            if key == 'external-subnet':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if ip_helper.is_ipv4_in_cidr(external_ip, value):
                        value_match = True

                if not value_match:
                    return False

            if key == 'external-string':
                key_found = True
                value_match = False
                for external_ip in service_info['external_ips']:
                    if filter_helper.match_string(external_ip, value):
                        value_match = True

                if filter_helper.match_string(value, service_info['external_name']):
                    value_match = True

                if not value_match:
                    return False

            if key == 'port':
                key_found = True
                value_match = False
                for port in service_info['port']:
                    if filter_helper.match_integer(value, port['port']):
                        value_match = True

                if not value_match:
                    return False

            if key == 'special':
                key_found = True
                if not filter_helper.match_string(value, service_info['special']):
                    return False

            if key == 'selector':
                key_found = True
                (selector_key, selector_value) = value.split(':')
                if selector_key not in service_info['selector']:
                    return False

                if not filter_helper.match_string(selector_value, service_info['selector'][selector_key]):
                    return False

            if not key_found:
                self.log.error(
                    'match_service',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_services(self, object_filter=None, endpoint_info=False, pod_info=False, return_mo=False, cache_enabled=True):
        all_services = self.get_services_info(cache_enabled=cache_enabled)
        if all_services is None:
            return None

        services = []

        endpoints = None
        if endpoint_info:
            endpoints = self.get_endpoints(cache_enabled=cache_enabled)

        pods = None
        if not endpoint_info and pod_info:
            pods = self.get_pods(cache_enabled=cache_enabled)

        for service_info in all_services:
            if not self.match_service(service_info['info'], object_filter):
                continue

            if return_mo:
                services.append(
                    service_info['mo']
                )
                continue

            if endpoints is not None:
                service_info['info']['podT'] = []
                service_info['info']['addressT'] = []
            
                for endpoint in endpoints:
                    if filter_helper.is_dict_in_dict(service_info['info']['label'], endpoint['label']):
                        service_info['info']['podT'] = copy.deepcopy(endpoint['podT'])
                        service_info['info']['addressT'] = copy.deepcopy(endpoint['addressT'])

            if pods is not None:
                service_info['info']['podT'] = []
                service_info['info']['pod'] = []
                if len(service_info['info']['selector']) > 0:
                    if pods is not None:
                        for pod in pods:
                            if self.check_pod_with_label(pod, service_info['info']['selector']):
                                service_info['info']['pod'].append(pod)
                                service_info['info']['podT'].append(
                                    pod['name']
                                )

            services.append(
                service_info['info']
            )

        return services

    def is_service(self, namespace, name, cache_enabled=True):
        if self.get_service(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def is_service_with_special_label(self, label, cache_enabled=True):
        services_mo = self.get_services_with_special_label(
            label,
            return_mo=True,
            cache_enabled=cache_enabled
        )
        if services_mo is not None and len(services_mo) > 0:
            return True
        return False

    def check_service_with_label(self, service_info, labels):
        if 'label' not in service_info:
            return False
        
        for label in labels:
            if label not in service_info['label']:
                return False
            
            if service_info['label'][label] != labels[label]:
                return False
            
        return True

    def get_service(self, namespace, name, endpoint_info=False, pod_info=False, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        services = self.get_services(
            object_filter=object_filter,
            endpoint_info=endpoint_info,
            pod_info=pod_info,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if services is None:
            return None

        if len(services) == 1:
            return services[0]

        return None

    def get_service_node_ip_port(self, namespace, name, cache_enabled=True, port_name=None):
        service_info = self.get_service(
            namespace,
            name,
            cache_enabled=cache_enabled
        )
        if service_info is None:
            return None, None

        if service_info['type'] != 'NodePort':
            self.log.error(
                'k8s.get_service_node_ip_port',
                'Unexpected service type: %s/%s' % (namespace, name)
            )
            return None, None

        if len(service_info['port']) == 0:
            self.log.error(
                'k8s.get_service_node_ip_port',
                'Unexpected no port: %s/%s' % (namespace, name)
            )
            return None, None

        if len(service_info['port']) > 1 and port_name is None:
            self.log.error(
                'k8s.get_service_node_ip_port',
                'Port name not defined and multiple ports available: %s/%s' % (namespace, name)
            )
            return None, None

        node_ip = self.get_any_worker_node_ip()
        if node_ip is None:
            self.log.error(
                'k8s.get_service_node_ip_port',
                'No ready worker node found'
            )
            return None, None

        for port_info in service_info['port']:
            if port_name is None or port_info['name'] == port_name:
                return node_ip, port_info['node_port']

        self.log.error(
            'k8s.get_service_node_ip_port',
            'No port found: %s/%s with port name %s' % (namespace, name, port_name)
        )
        return None, None

    def get_services_with_special_label(self, label, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'special:%s' % (
                label
            )
        )
        services_mo = self.get_services(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        return services_mo

    def get_service_base_body(self, namespace, name, labels=None):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Service'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]

        body['spec'] = {}
        return body
