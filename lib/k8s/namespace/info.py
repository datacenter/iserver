import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sNamespaceInfo():
    def __init__(self):
        self.namespace = None

    def get_namespace_info(self, namespace_mo):
        if namespace_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            namespace_mo
        )
        info.update(metadata_info)

        info['phase'] = self.get(namespace_mo, 'status:phase')
        if info['phase'] is not None and info['phase'] == 'Active':
            info['__Output']['phase'] = 'Green'
        else:
            info['__Output']['phase'] = 'Red'

        return info

    def get_namespaces_info(self, cache_enabled=True):
        if cache_enabled:
            if self.namespace is not None:
                return self.namespace

        managed_objects = self.get_namespace_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.namespace = []
        for managed_object in managed_objects:
            namespace_info = {}
            namespace_info['info'] = self.get_namespace_info(
                managed_object
            )
            namespace_info['mo'] = managed_object
            self.namespace.append(
                namespace_info
            )

        return self.namespace

    def match_namespace(self, namespace_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, namespace_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_namespace',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_namespaces(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_namespaces = self.get_namespaces_info(cache_enabled=cache_enabled)
        if all_namespaces is None:
            return None

        namespaces = []

        for namespace_info in all_namespaces:
            if not self.match_namespace(namespace_info['info'], object_filter):
                continue

            if return_mo:
                namespaces.append(
                    namespace_info['mo']
                )
                continue

            namespaces.append(
                namespace_info['info']
            )

        return namespaces

    def is_namespace(self, name, cache_enabled=True):
        if self.get_namespace(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_namespace(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        namespaces = self.get_namespaces(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if namespaces is None:
            return None

        if len(namespaces) == 1:
            return namespaces[0]

        return None

    def is_namespace_label(self, namespace, label_key, label_value=None, cache_enabled=True):
        namespace_mo = self.get_namespace(namespace, cache_enabled=cache_enabled, return_mo=True)
        if namespace_mo is None:
            return False

        labels = self.get(namespace_mo, 'metadata:labels')
        if labels is None:
            return False

        for label in labels:
            if label == label_key:
                if label_value is None:
                    return True

                if labels[label] == label_value:
                    return True

        return False

    def check_namespace_usage_and_state(self, namespace, my_output=None, show_details=False, underline=False, before_newline=True):
        used = False
        state = {}
        state['pod'] = True
        state['deployment'] = True
        state['replica_set'] = True
        state['daemon_set'] = True
        state['pvc'] = True

        if my_output is not None:
            my_output.default('Namespace [%s] resources' % (namespace), underline=underline, before_newline=before_newline)
        
        object_filter = ['namespace:%s' % (namespace)]

        pods = self.get_pods(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to check pod')

        if pods is not None:
            if len(pods) == 0:
                if my_output is not None:
                    my_output.default('- no pods')
            else:
                used = True
                for pod in pods:
                    if not pod['running']:
                        state['pod'] = False

                if my_output is not None:
                    if show_details:
                        my_output.default('- pod')
                        for pod in pods:
                            my_output.default(
                                '\t[%s] [%s] [%s]' % (
                                    pod['namespace_name'], 
                                    pod['container_state_summary'],
                                    my_output.add_color(pod['phaseT'], pod['__Output']['phaseT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- pods [%s]' % (len(pods)))

        deployments = self.get_deployments(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if deployments is None:
            if my_output is not None:
                my_output.error('Failed to check deployment')

        if deployments is not None:
            if len(deployments) == 0:
                if my_output is not None:
                    my_output.default('- no deployments')
            else:
                used = True
                for deployment in deployments:
                    if not deployment['ready']:
                        state['deployment'] = False

                if my_output is not None:
                    if show_details:
                        my_output.default('- deployment')
                        for deployment in deployments:
                            my_output.default(
                                '\t[%s] [%s]' % (
                                    deployment['namespace_name'], 
                                    my_output.add_color(deployment['readyT'], deployment['__Output']['readyT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- deployments [%s]' % (len(deployments)))

        daemon_sets = self.get_daemon_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if daemon_sets is None:
            if my_output is not None:
                my_output.error('Failed to check daemon set')

        if daemon_sets is not None:
            if len(daemon_sets) == 0:
                if my_output is not None:
                    my_output.default('- no daemon sets')
            else:
                used = True
                for daemon_set in daemon_sets:
                    if not daemon_set['ready']:
                        state['ready'] = False

                if my_output is not None:
                    if show_details:
                        my_output.default('- daemon set')
                        for daemon_set in daemon_sets:
                            my_output.default(
                                '\t[%s] Scheduled [%s] Available [%s]' % (
                                    daemon_set['namespace_name'], 
                                    my_output.add_color(daemon_set['scheduled_summary'], daemon_set['__Output']['scheduled_summary']),
                                    my_output.add_color(daemon_set['available_summary'], daemon_set['__Output']['available_summary'])
                                )
                            )

                    if not show_details:
                        my_output.default('- daemon sets [%s]' % (len(daemon_sets)))

        replica_sets = self.get_replica_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if replica_sets is None:
            if my_output is not None:
                my_output.error('Failed to check replica set')

        if replica_sets is not None:
            if len(replica_sets) == 0:
                if my_output is not None:
                    my_output.default('- no replica sets')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- replica set')
                        for replica_set in replica_sets:
                            my_output.default(
                                '\t[%s] [%s]' % (
                                    replica_set['namespace_name'], 
                                    my_output.add_color(replica_set['replicasT'], replica_set['__Output']['replicasT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- replica sets [%s]' % (len(replica_sets)))

        services = self.get_services(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if services is None:
            if my_output is not None:
                my_output.error('Failed to check service')

        if services is not None:
            if len(services) == 0:
                if my_output is not None:
                    my_output.default('- no services')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- service')
                        for service in services:
                            my_output.default(
                                '\t[%s] [%s] [%s]' % (
                                    service['namespace_name'], 
                                    service['type'], 
                                    service['ports']
                                )
                            )

                    if not show_details:
                        my_output.default('- services [%s]' % (len(services)))

        pvcs = self.get_pvcs(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if pvcs is None:
            if my_output is not None:
                my_output.error('Failed to check pvc')

        if pvcs is not None:
            if len(pvcs) == 0:
                if my_output is not None:
                    my_output.default('- no pvcs')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- pvc')
                        for pvc in pvcs:
                            my_output.default(
                                '\t[%s]' % (
                                    pvc['namespace_name']
                                )
                            )

                    if not show_details:
                        my_output.default('- pvc [%s]' % (len(pvcs)))


        return used
    
    def get_namespace_body(self, name, labels=None):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Namespace'
        body['metadata'] = {}
        body['metadata']['name'] = name
        if labels is not None:
            body['metadata']['labels'] = {}
            for key in labels:
                body['metadata']['labels'][key] = labels[key]

        return body

    def create_namespace(
            self,
            name,
            labels=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if labels is not None and len(labels) == 0:
            labels = None
            
        if my_output is not None:
            my_output.default('Create Namespace', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))
            if labels is not None:
                my_output.default('- labels')
                for label in labels:
                    my_output.default('\t%s:%s' % (label, labels[label]))

        if self.is_namespace(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already defined')
        else:
            body = self.get_namespace_body(
                name,
                labels=labels
            )
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            if confirmation:
                if not get_confirmation():
                    return False

            if not self.create_namespace_mo_from_body(body):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
            
            if my_output is not None:
                my_output.default('Namespace created', before_newline=True, after_newline=True)

            if wait:
                if my_output is not None:
                    my_output.default('Wait for namespace [timeout:60]...')

                if not self.wait_namespace(name, max_time=60):
                    if my_output is not None:
                        my_output.error('Timed out')
                    
                    return False

        if labels is not None:
            if my_output is not None:
                my_output.default('Check labels', before_newline=True)
            for key in labels:
                if my_output is not None:
                    my_output.default('- %s:%s' % (key, labels[key]))

                if not self.is_namespace_label(name, key, cache_enabled=False):
                    continue

                if not self.add_namespace_label(name, key, labels[key]):
                    if my_output is not None:
                        my_output.error('REST API failed')
                    return False

        return True        

    def wait_namespace(self, namespace, max_time=60):
        start_time = int(time.time())
        while True:
            namespace_info = self.get_namespace(
                namespace,
                cache_enabled=False
            )
            if namespace_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_namespace',
                    'Max time reached: %s' % (namespace)
                )
                return False

            time.sleep(5)

    def remove_namespace_finalizers(self, namespace):
        namespace_mo = self.get_namespace(namespace, return_mo=True, cache_enabled=False)
        if namespace_mo is None:
            return False
        
        if 'finalizers' not in namespace_mo['spec']:
            return True
        
        del namespace_mo['spec']['finalizers']
        return self.set_namespace_mo(namespace_mo)
    
    def delete_namespace(self, namespace, my_output=None, check_usage=True, wait=True, finalizers=False):
        if my_output is not None:
            my_output.default('Delete Namespace', before_newline=True, underline=True)
            my_output.default('- name: %s' % (namespace))

        if not self.is_namespace(namespace):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
    
        if check_usage:
            used = self.check_namespace_usage_and_state(
                namespace, 
                my_output=my_output, 
                show_details=True,
                underline=False
            )
            if used:
                if my_output is not None:
                    my_output.error('Namespace used and cannot be deleted')

                return False
    
        success = self.delete_namespace_mo(namespace)
        if not success:
            if my_output is not None:
                my_output.error('Delete API failed')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no namespace')

            if not self.wait_no_namespace(namespace):
                if my_output is not None:
                    my_output.error('Timed out')

                if not finalizers:
                    return False
                
                if my_output is not None:
                    my_output.default('Remove finalizers')

                if not self.remove_namespace_finalizers(namespace):
                    if my_output is not None:
                        my_output.error('REST API failed')
                    return False
                
                if not self.wait_no_namespace(namespace):
                    if my_output is not None:
                        my_output.error('Giving up')

                    return False

        return True

    def wait_no_namespace(self, namespace, max_time=60):
        start_time = int(time.time())
        while True:
            namespace_info = self.get_namespace(
                namespace,
                cache_enabled=False
            )
            if namespace_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_namespace',
                    'Max time reached: %s' % (namespace)
                )
                return False

            time.sleep(5)