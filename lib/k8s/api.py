import os
import time
import json
import traceback
import yaml
from lib import filter_helper
from kubernetes import config
from kubernetes import client
from kubernetes.config import kube_config
from menu.common import get_confirmation

# https://github.com/openshift/openshift-restclient-python
from openshift.dynamic import DynamicClient
from urllib3.exceptions import MaxRetryError


class K8sApi():
    def __init__(self, kubeconfig_filename, cluster_type='standard'):
        self.kubeconfig_filename = kubeconfig_filename
        self.cluster_type = cluster_type
        self.api = {}
        self.api_timeout_seconds = 3
        self.connect_timeout_seconds = 3
        self.api_retries = 1
        self.kind_get_all = {
            'Node': 'list_node',
            'Pod': 'list_pod_for_all_namespaces'
        }
        self.kind_get_namespace = {
            'Pod': 'list_namespaced_pod'
        }
        self.kind_get_namespace_name = {
            'Pod': 'read_namespaced_pod',
            'Node': 'read_node'
        }
        self.kind_create_namespace_name = {
            'Pod': 'create_namespaced_pod'
        }
        self.kind_create_name = {           
        }
        self.kind_replace_namespace_name = { 
            'Pod': 'replace_namespaced_pod'
        }
        self.kind_replace_name = {           
        }
        self.kind_patch_namespace_name = { 
            'Deployment': 'patch_namespaced_deployment'
        }
        self.kind_patch_name = {           
        }
        self.kind_delete_namespace_name = { 
            'Deployment': 'delete_namespaced_deployment'
        }
        self.kind_delete_name = {           
        }

    def check_api(self):
        if not self.get_node_mo(cache_enabled=False, fast=True):
            return False
        return True

    def get_api_kind(self, kind, api_type='v1'):
        if kind in self.kind_get_all or kind in self.kind_get_namespace or kind in self.kind_get_namespace_name:
            return self.get_api(api_type=api_type)
        
        return self.get_api(self.cluster_type, api_type=api_type)
    
    def get_api(self, cluster_type='standard', api_type='v1'):
        if cluster_type not in ['standard', 'ocp']:
            self.log.error(
                'get_api',
                'Unsupported cluster type: %s' % (cluster_type)
            )
            return None

        if cluster_type == 'standard':
            if api_type == 'v1':
                return self.get_api_standard()

            if api_type == 'apps':
                return self.get_api_apps()

            if api_type == 'version':
                return self.get_api_version()

            if api_type == 'admission':
                return self.get_api_admission()

        if cluster_type == 'ocp':
            return self.get_api_ocp()

        return None

    def get_api_standard(self):
        if 'standard' in self.api and self.api['standard'] is not None:
            return self.api['standard']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_standard',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            my_config = client.Configuration()
            my_config.verify_ssl = False
            my_config.retries = self.api_retries

            with open(self.kubeconfig_filename, 'r', encoding='utf-8') as file_handler:
                configuration_yaml = yaml.safe_load(file_handler.read())

            k8_loader = kube_config.KubeConfigLoader(
                configuration_yaml
            )
            k8_loader.load_and_set(my_config)

            my_client = client.ApiClient(
                configuration=my_config
            )
            self.api['standard'] = client.CoreV1Api(
                api_client=my_client
            )

            # response = self.api['standard'].list_namespace(
            #     timeout_seconds=self.api_timeout_seconds,
            #     _request_timeout=self.connect_timeout_seconds
            # )

            self.log.k8s(
                'connect.standard',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except MaxRetryError:
            self.log.error(
                'k8s.get_api_standard',
                'Connection timed out'
            )
            return None

        except BaseException:
            self.log.error(
                'k8s.get_api_standard',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_standard', traceback.format_exc())
            return None

        return self.api['standard']

    def get_api_apps(self):
        if 'apps' in self.api and self.api['apps'] is not None:
            return self.api['apps']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_apps',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            my_config = client.Configuration()
            my_config.verify_ssl = False
            my_config.retries = self.api_retries

            with open(self.kubeconfig_filename, 'r', encoding='utf-8') as file_handler:
                configuration_yaml = yaml.safe_load(file_handler.read())

            k8_loader = kube_config.KubeConfigLoader(
                configuration_yaml
            )
            k8_loader.load_and_set(my_config)

            my_client = client.ApiClient(
                configuration=my_config
            )
            self.api['apps'] = client.AppsV1Api(
                api_client=my_client
            )

            self.log.k8s(
                'connect.apps',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except MaxRetryError:
            self.log.error(
                'k8s.get_api_apps',
                'Connection timed out'
            )
            return None

        except BaseException:
            self.log.error(
                'k8s.get_api_apps',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_apps', traceback.format_exc())
            return None

        return self.api['apps']

    def get_api_version(self):
        if 'version' in self.api and self.api['version'] is not None:
            return self.api['version']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_version',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            config.load_kube_config(self.kubeconfig_filename)
            self.api['version'] = client.VersionApi()

            self.log.k8s(
                'connect.version',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'k8s.get_api_version',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_version', traceback.format_exc())
            return None

        return self.api['version']

    def get_api_admission(self):
        if 'admission' in self.api and self.api['admission'] is not None:
            return self.api['admission']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_admission',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            config.load_kube_config(self.kubeconfig_filename)
            self.api['admission'] = client.AdmissionregistrationV1Api()

            self.log.k8s(
                'connect.admission',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error(
                'k8s.get_api_admission',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_admission', traceback.format_exc())
            return None

        return self.api['admission']

    def get_api_ocp(self):
        if 'ocp' in self.api and self.api['ocp'] is not None:
            return self.api['ocp']

        if not os.path.isfile(self.kubeconfig_filename):
            self.log.error(
                'k8s.get_api_ocp',
                'Kubeconfig file not found: %s' % (self.kubeconfig_filename)
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            my_config = client.Configuration()
            my_config.retries = self.api_retries

            with open(self.kubeconfig_filename, 'r', encoding='utf-8') as file_handler:
                configuration_yaml = yaml.safe_load(file_handler.read())

            k8_loader = kube_config.KubeConfigLoader(
                configuration_yaml
            )
            k8_loader.load_and_set(my_config)

            my_client = client.ApiClient(
                configuration=my_config
            )
            self.api['ocp'] = DynamicClient(my_client)

            self.log.k8s(
                'connect.ocp',
                '-',
                True,
                int(time.time() * 1000) - start_time
            )

        except MaxRetryError:
            self.log.error(
                'k8s.get_api_standard',
                'Connection timed out'
            )
            return None

        except BaseException:
            self.log.error(
                'k8s.get_api_ocp',
                'Kubeconfig file failed: %s' % (self.kubeconfig_filename)
            )
            self.log.error('k8s.get_api_standard', traceback.format_exc())
            return None

        return self.api['ocp']

    def wait_mcp_cluster_restart(self, initial_nodes_state, my_output=None, max_time=3600, max_failed_count=10):
        if my_output is not None:
            my_output.default('Wait for mcp-initiated cluster nodes restart', before_newline=True, underline=True)
            my_output.default('Max time: %s seconds' % (max_time))

        start_time = int(time.time())
        failed_count = 0

        last_node_status = {}
        for item in initial_nodes_state:
            last_node_status[item['name']] = item['node_status']

        nodes_unreachable = []
        nodes_restarted = []

        while True:
            node_info = self.get_nodes(
                cache_enabled=False
            )
            if node_info is None:
                failed_count += 1
                if failed_count == max_failed_count:
                    if my_output is not None:
                        my_output.default('API failed last %s consecutive attempts -- assumption of last cluster node restart' % (failed_count))
                    return True, None

            if node_info is not None:
                failed_count = 0
                for item in node_info:
                    if last_node_status[item['name']] != item['node_status']:
                        last_node_status[item['name']] = item['node_status']
                        if my_output is not None:
                            my_output.default('Node [%s] Status %s' % (
                                item['name'],
                                item['node_status']
                            ))

                        if 'unreachable' in item['node_status']:
                            if item['name'] not in nodes_unreachable:
                                nodes_unreachable.append(
                                    item['name']
                                )
                                if my_output is not None:
                                    my_output.default('Node [%s] down on restart' % (
                                        item['name']
                                    ))

                        if 'Ready' in item['node_status'] and len(item['node_status']) == 1:
                            if item['name'] in nodes_unreachable:
                                if item['name'] not in nodes_restarted:
                                    nodes_restarted.append(
                                        item['name']
                                    )
                                    if my_output is not None:
                                        my_output.default('Node [%s] back operational' % (
                                            item['name']
                                        ))

            if len(nodes_restarted) == len(initial_nodes_state):
                my_output.default('All nodes restarted')
                return True, None

            duration = int(time.time()) - start_time
            if duration > max_time:
                if my_output is not None:
                    my_output.error('Timed out')
                self.log.error(
                    'k8s.wait_no_api',
                    'Max time reached'
                )

                failed_nodes = []
                for node in initial_nodes_state:
                    if node not in nodes_restarted:
                        failed_count.append(node)

                return False, failed_nodes

            time.sleep(5)

    def wait_no_api(self, max_time=600, max_failed_count=5):
        start_time = int(time.time())
        failed_count = 0
        while True:
            node_info = self.get_nodes(
                cache_enabled=False
            )
            if node_info is None:
                failed_count += 1
                if failed_count == max_failed_count:
                    return True

            if node_info is not None:
                failed_count = 0

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_api',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_api(self, max_time=600, min_success_count=3):
        start_time = int(time.time())
        success_count = 0
        while True:
            node_info = self.get_nodes(
                cache_enabled=False
            )
            if node_info is None:
                success_count = 0
                
            if node_info is not None:
                success_count += 1
                if success_count == min_success_count:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_api',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def get_api_exception_reason(self, err):
        try:
            reason = json.loads(err.body.decode('utf-8'))['details']['causes'][0]['message']
        except BaseException:
            reason = 'Reason unknown'
        
        return reason
    
    def get_namespaced_resources(self, kind, api_version, managed_objects, namespaced_objects, namespace=None, name=None):
        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            return None, managed_objects, namespaced_objects

        start_time = int(time.time() * 1000)

        # All kind objects
        if namespace is None and name is None:
            try:
                if kind in self.kind_get_all:
                    response_mo = getattr(api_handler, self.kind_get_all[kind])(
                        timeout_seconds=self.api_timeout_seconds
                    )
                    response = []
                    for item in response_mo.items:
                        response.append(
                            self.convert_object(item.to_dict())
                        )

                if kind not in self.kind_get_all:
                    response = api_handler.resources.get(
                        api_version=api_version,
                        kind=kind
                    ).get().to_dict()['items']

                self.log.k8s(
                    'get',
                    '%s [%s]' % (kind, api_version),
                    True,
                    int(time.time() * 1000) - start_time
                )
            except BaseException:
                self.log.error('k8s.get_namespaced_resources', traceback.format_exc())
                self.log.k8s(
                    'get',
                    '%s [%s]' % (kind, api_version),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return None, managed_objects, namespaced_objects

        # All kind objects from namespace
        if namespace is not None and name is None:
            try:
                if kind in self.kind_get_namespace:
                    response_mo = getattr(api_handler, self.kind_get_namespace[kind])(
                        namespace=namespace,
                        timeout_seconds=self.api_timeout_seconds
                    )
                    response = []
                    for item in response_mo.items:
                        response.append(
                            self.convert_object(item.to_dict())
                        )

                if kind not in self.kind_get_namespace:
                    response = api_handler.resources.get(
                        api_version=api_version,
                        kind=kind
                    ).get(namespace=namespace).to_dict()['items']

                self.log.k8s(
                    'get',
                    '%s [%s] [ns:%s]' % (kind, api_version, namespace),
                    True,
                    int(time.time() * 1000) - start_time
                )
            except BaseException:
                self.log.error('k8s.get_namespaced_resources', traceback.format_exc())
                self.log.k8s(
                    'get',
                    '%s [%s] [ns:%s]' % (kind, api_version, namespace),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return None, managed_objects, namespaced_objects

        # Single object
        if namespace is not None and name is not None:
            try:
                if kind in self.kind_get_namespace_name:
                    response_mo = getattr(api_handler, self.kind_get_namespace_name[kind])(
                        name,
                        namespace
                    )
                    response = self.convert_object(response_mo.to_dict())

                if kind not in self.kind_get_namespace_name:
                    response = api_handler.resources.get(
                        api_version=api_version,
                        kind=kind
                    ).get(name=name, namespace=namespace).to_dict()

                self.log.k8s(
                    'get',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    True,
                    int(time.time() * 1000) - start_time
                )
            except BaseException:
                self.log.error('k8s.get_namespaced_resources', traceback.format_exc())
                self.log.k8s(
                    'get',
                    '%s [%s] [ns:%s]' % (kind, api_version, namespace),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return None, managed_objects, namespaced_objects
            
            return response, managed_objects, namespaced_objects

        return self.untangle_namespaced_mo(response, kind, namespace, managed_objects, namespaced_objects)

    def untangle_namespaced_mo(self, response, kind, namespace, managed_objects, namespaced_objects):
        if namespace is not None:
            namespaced_objects[namespace] = response
            return namespaced_objects[namespace], managed_objects, namespaced_objects
        
        managed_objects = []
        for item in response:
            managed_objects.append(item)
            if 'namespace' in item['metadata']:
                namespace_mo = item['metadata']['namespace']
                if namespace_mo not in namespaced_objects:
                    namespaced_objects[namespace] = []
                namespaced_objects[namespace].append(
                    item
                )

        self.log.k8s_mo(
            kind,
            managed_objects
        )

        return managed_objects, managed_objects, namespaced_objects
    
    def get_namespaced_cache(self, cache_enabled, namespace, name, managed_objects, namespaced_objects):
        if not cache_enabled:
            return False, None
        
        if namespace is None:
            if managed_objects is None:
                return False, None
            return True, managed_objects
            
        if namespace not in namespaced_objects:
            return False, None
        
        if name is None:
            return True, namespaced_objects[namespace]

        for item in namespaced_objects[namespace]:
            if item['metadata']['name'] == name:
                return True, item
            
        return True, None
    
    def get_resources(self, kind, api_version, managed_objects, name=None, fast=False):
        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            return None, managed_objects

        start_time = int(time.time() * 1000)
        timeout = self.api_timeout_seconds
        if fast:
            timeout = 1

        # All kind objects
        if name is None:
            try:
                if kind in self.kind_get_all:
                    response_mo = getattr(api_handler, self.kind_get_all[kind])(
                        timeout_seconds=timeout
                    )
                    response = []
                    for item in response_mo.items:
                        response.append(
                            self.convert_object(item.to_dict())
                        )

                if kind not in self.kind_get_all:
                    response = api_handler.resources.get(
                        api_version=api_version,
                        kind=kind
                    ).get().to_dict()['items']

                self.log.k8s(
                    'get',
                    '%s [%s]' % (kind, api_version),
                    True,
                    int(time.time() * 1000) - start_time
                )
            except BaseException:
                self.log.error('k8s.get_resources', traceback.format_exc())
                self.log.k8s(
                    'get',
                    '%s [%s]' % (kind, api_version),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return None, managed_objects

        # Single object
        if name is not None:
            try:
                if kind in self.kind_get_namespace_name:
                    response_mo = getattr(api_handler, self.kind_get_namespace_name[kind])(
                        name
                    )
                    response = self.convert_object(response_mo.to_dict())

                if kind not in self.kind_get_namespace_name:
                    response = api_handler.resources.get(
                        api_version=api_version,
                        kind=kind
                    ).get(name=name).to_dict()

                self.log.k8s(
                    'get',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    True,
                    int(time.time() * 1000) - start_time
                )
            except BaseException:
                self.log.error('k8s.get_resources', traceback.format_exc())
                self.log.k8s(
                    'get',
                    '%s [%s]' % (kind, api_version),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return None, managed_objects
            
            return response, managed_objects

        return self.untangle_mo(response, kind, managed_objects)

    def untangle_mo(self, response, kind, managed_objects):
        managed_objects = []
        for item in response:
            managed_objects.append(item)

        self.log.k8s_mo(
            kind,
            managed_objects
        )

        return managed_objects, managed_objects

    def get_cache(self, cache_enabled, name, managed_objects):
        if not cache_enabled:
            return False, None
        
        if name is None:
            if managed_objects is None:
                return False, None
            return True, managed_objects
            
        for item in managed_objects:
            if item['metadata']['name'] == name:
                return True, item
            
        return True, None

    def create_resource(self, body, object_name=None, my_output=None, confirmation=False):
        kind = filter_helper.get(body, 'kind')
        api_version = filter_helper.get(body, 'apiVersion')
        namespace = filter_helper.get(body, 'metadata:namespace')
        name = filter_helper.get(body, 'metadata:name')

        if kind is None or api_version is None or name is None:
            if my_output is not None:
                my_output.error('Body parse failed')
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            return False

        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            if my_output is not None:
                my_output.error('Kubernetes api not ready')
            return False

        if my_output is not None:
            my_output.default('Create %s' % (kind), before_newline=True, underline=True)
            if namespace is not None:
                my_output.default('- namespace: %s' % (namespace))
            if name is not None:
                my_output.default('- name: %s' % (name))

        if object_name is not None:
            if namespace is None:
                found = getattr(self, 'is_%s' % (object_name))(
                    name, cache_enabled=False
                )
            else:
                found = getattr(self, 'is_%s' % (object_name))(
                    namespace, name, cache_enabled=False
                )

            if found:
                if my_output is not None:
                    my_output.default('- %s' % (my_output.add_color('already created', 'Green')))
                    
                return True
        
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            if confirmation:
                if not get_confirmation():
                    return False

        start_time = int(time.time() * 1000)

        if namespace is None:
            try:
                if kind in self.kind_create_name:
                    response = getattr(api_handler, self.kind_create_name[kind])(
                        body
                    )

                if kind not in self.kind_create_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.create(
                        body=body
                    )

                self.log.k8s(
                    'create',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s] %s' % (
                            kind,
                            name,
                            my_output.add_color('created', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.create_resource', traceback.format_exc())
                self.log.k8s(
                    'create',
                    '%s [%s] [name:%s] [response:%s]' % (kind, api_version, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        if namespace is not None:
            try:
                if kind in self.kind_create_namespace_name:
                    response = getattr(api_handler, self.kind_create_namespace_name[kind])(
                        namespace,
                        body
                    )

                if kind not in self.kind_create_namespace_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.create(
                        body=body,
                        namespace=namespace
                    )

                self.log.k8s(
                    'create',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s/%s] %s' % (
                            kind,
                            namespace,
                            name,
                            my_output.add_color('created', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.create_resource', traceback.format_exc())
                self.log.k8s(
                    'create',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        return True

    def patch_resource(self, body, object_name=None, my_output=None, confirmation=False):
        kind = filter_helper.get(body, 'kind')
        api_version = filter_helper.get(body, 'apiVersion')
        namespace = filter_helper.get(body, 'metadata:namespace')
        name = filter_helper.get(body, 'metadata:name')

        if kind is None or api_version is None or name is None:
            if my_output is not None:
                my_output.error('Body parse failed')
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            return False

        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            if my_output is not None:
                my_output.error('Kubernetes api not ready')
            return False

        if my_output is not None:
            my_output.default('Patch %s' % (kind), before_newline=True, underline=True)
            if namespace is not None:
                my_output.default('- namespace: %s' % (namespace))
            if name is not None:
                my_output.default('- name: %s' % (name))

        if object_name is not None:
            if namespace is None:
                found = getattr(self, 'is_%s' % (object_name))(
                    name, cache_enabled=False
                )
            else:
                found = getattr(self, 'is_%s' % (object_name))(
                    namespace, name, cache_enabled=False
                )

            if not found:
                if my_output is not None:
                    my_output.default('- %s' % (my_output.add_color('not found', 'Red')))
                    
                return False
        
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            if confirmation:
                if not get_confirmation():
                    return False

        start_time = int(time.time() * 1000)

        if namespace is None:
            try:
                if kind in self.kind_patch_name:
                    response = getattr(api_handler, self.kind_patch_name[kind])(
                        name,
                        body
                    )

                if kind not in self.kind_patch_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.patch(
                        body=body,
                        name=name,
                        content_type='application/merge-patch+json'
                    )

                self.log.k8s(
                    'patch',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s] %s' % (
                            kind,
                            name,
                            my_output.add_color('patched', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.patch_resource', traceback.format_exc())
                self.log.k8s(
                    'patch',
                    '%s [%s] [name:%s] [response:%s]' % (kind, api_version, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        if namespace is not None:
            try:
                if kind in self.kind_patch_namespace_name:
                    response = getattr(api_handler, self.kind_patch_namespace_name[kind])(
                        name,
                        namespace,
                        body
                    )

                if kind not in self.kind_patch_namespace_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.patch(
                        body=body,
                        namespace=namespace,
                        name=name,
                        content_type='application/merge-patch+json'
                    )

                self.log.k8s(
                    'patch',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s/%s] %s' % (
                            kind,
                            namespace,
                            name,
                            my_output.add_color('patched', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.patch_resource', traceback.format_exc())
                self.log.k8s(
                    'patch',
                    '%s [%s] [ns:%s] [name:%s] [response:%s]' % (kind, api_version, namespace, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        return True

    def replace_resource(self, body, object_name=None, my_output=None, confirmation=False):
        kind = filter_helper.get(body, 'kind')
        api_version = filter_helper.get(body, 'apiVersion')
        namespace = filter_helper.get(body, 'metadata:namespace')
        name = filter_helper.get(body, 'metadata:name')

        if kind is None or api_version is None or name is None:
            if my_output is not None:
                my_output.error('Body parse failed')
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            return False

        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            if my_output is not None:
                my_output.error('Kubernetes api not ready')
            return False

        if my_output is not None:
            my_output.default('Replace %s' % (kind), before_newline=True, underline=True)
            if namespace is not None:
                my_output.default('- namespace: %s' % (namespace))
            if name is not None:
                my_output.default('- name: %s' % (name))

        if object_name is not None:
            if namespace is None:
                found = getattr(self, 'is_%s' % (object_name))(
                    name, cache_enabled=False
                )
            else:
                found = getattr(self, 'is_%s' % (object_name))(
                    namespace, name, cache_enabled=False
                )

            if not found:
                if my_output is not None:
                    my_output.default('- %s' % (my_output.add_color('not found', 'Red')))
                    
                return False
        
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')
            if confirmation:
                if not get_confirmation():
                    return False

        start_time = int(time.time() * 1000)

        if namespace is None:
            try:
                if kind in self.kind_replace_name:
                    response = getattr(api_handler, self.kind_replace_name[kind])(
                        name,
                        body
                    )

                if kind not in self.kind_replace_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.replace(
                        body=body,
                        name=name
                    )

                self.log.k8s(
                    'replace',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s] %s' % (
                            kind,
                            name,
                            my_output.add_color('replaced', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.replace_resource', traceback.format_exc())
                self.log.k8s(
                    'replace',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        if namespace is not None:
            try:
                if kind in self.kind_replace_namespace_name:
                    response = getattr(api_handler, self.kind_replace_namespace_name[kind])(
                        name,
                        namespace,
                        body
                    )

                if kind not in self.kind_replace_namespace_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.replace(
                        body=body,
                        namespace=namespace,
                        name=name
                    )

                self.log.k8s(
                    'replace',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '%s [%s/%s] %s' % (
                            kind,
                            namespace,
                            name,
                            my_output.add_color('replaced', 'Green')
                        )
                    )

            except BaseException:
                if my_output is not None:
                    my_output.error('Kubernetes api exception')

                self.log.error('k8s.replace_resource', traceback.format_exc())
                self.log.k8s(
                    'replace',
                    '%s [%s] [ns:%s] [name:%s] [response:%s]' % (kind, api_version, namespace, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        return True

    def delete_resource(self, kind, api_version, name, namespace=None, object_name=None, my_output=None):
        api_handler = self.get_api_kind(kind)
        if api_handler is None:
            if my_output is not None:
                my_output.error('Kubernetes api not ready')
            return False

        if my_output is not None:
            my_output.default('Delete %s' % (kind), before_newline=True, underline=True)
            if namespace is not None:
                my_output.default('- namespace: %s' % (namespace))
            if name is not None:
                my_output.default('- name: %s' % (name))

        if object_name is not None:
            if namespace is None:
                found = getattr(self, 'is_%s' % (object_name))(
                    name, cache_enabled=False
                )
            else:
                found = getattr(self, 'is_%s' % (object_name))(
                    namespace, name, cache_enabled=False
                )

            if not found:
                if my_output is not None:
                    my_output.default('- %s' % (my_output.add_color('already deleted', 'Green')))
                return True

        start_time = int(time.time() * 1000)

        if namespace is None:
            try:
                if kind in self.kind_delete_name:
                    response = getattr(api_handler, self.kind_delete_name[kind])(
                        name
                    )

                if kind not in self.kind_delete_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.delete(
                        name=name
                    )

                self.log.k8s(
                    'delete',
                    '%s [%s] [name:%s]' % (kind, api_version, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '- %s' % (my_output.add_color('deleted', 'Green'))
                    )

            except BaseException:
                if my_output is not None:
                    my_output.default(
                        '- delete %s' % (my_output.add_color('failed', 'Red'))
                    )

                self.log.error('k8s.delete_resource', traceback.format_exc())
                self.log.k8s(
                    'delete',
                    '%s [%s] [name:%s] [response:%s]' % (kind, api_version, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        if namespace is not None:
            try:
                if kind in self.kind_delete_namespace_name:
                    response = getattr(api_handler, self.kind_delete_namespace_name[kind])(
                        name,
                        namespace
                    )

                if kind not in self.kind_delete_namespace_name:
                    obj_list = api_handler.resources.get(
                        api_version=api_version, 
                        kind=kind
                    )
                    response = obj_list.delete(
                        namespace=namespace,
                        name=name
                    )

                self.log.k8s(
                    'delete',
                    '%s [%s] [ns:%s] [name:%s]' % (kind, api_version, namespace, name),
                    True,
                    int(time.time() * 1000) - start_time
                )

                if my_output is not None:
                    my_output.default(
                        '- %s' % (my_output.add_color('deleted', 'Green'))
                    )

            except BaseException:
                if my_output is not None:
                    my_output.default(
                        '- delete %s' % (my_output.add_color('failed', 'Red'))
                    )

                self.log.error('k8s.delete_resource', traceback.format_exc())
                self.log.k8s(
                    'delete',
                    '%s [%s] [ns:%s] [name:%s] [response:%s]' % (kind, api_version, namespace, name, str(response)),
                    False,
                    int(time.time() * 1000) - start_time
                )
                return False

        return True
