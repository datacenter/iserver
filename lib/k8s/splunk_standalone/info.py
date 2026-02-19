import time
import base64
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sSplunkStandaloneInfo():
    def __init__(self):
        self.splunk_standalone = None

    def get_splunk_standalone_info(self, splunk_standalone_mo):
        if splunk_standalone_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            splunk_standalone_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(splunk_standalone_mo, 'spec')
        info['status'] = self.get(splunk_standalone_mo, 'status')

        info['phase'] = self.get(splunk_standalone_mo, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_splunk_standalone_extended_info(self, info):
        info['urlT'] = []
        if 'pod' in info:
            if info['pod'] is None:
                info['__Output']['podTick'] = 'Red'
                info['podTick'] = '\u2717'

            if info['pod'] is not None:
                if not info['pod']['running']:
                    info['__Output']['podTick'] = 'Red'
                    info['podTick'] = '\u2717'
                else:
                    info['__Output']['podTick'] = 'Green'
                    info['podTick'] = '\u2713'

        if 'pvc' in info:
            if info['pvc'] is None:
                info['__Output']['pvcTick'] = 'Red'
                info['pvcTick'] = '---'

            if info['pvc'] is not None:
                ready = 0
                for item in info['pvc']:
                    if item['ready']:
                        ready += 1

                if ready > 0 and ready == len(info['pvc']):
                    info['__Output']['pvcTick'] = 'Green'
                else:
                    info['__Output']['pvcTick'] = 'Red'

                info['pvcTick'] = '%s/%s' % (ready, len(info['pvc']))

        if 'service' in info:
            if info['service'] is None:
                info['__Output']['serviceTick'] = 'Red'
                info['serviceTick'] = '\u2717'

            if info['pod'] is not None:
                info['__Output']['serviceTick'] = 'Green'
                info['serviceTick'] = '\u2713'

        if 'route' in info:
            if info['route'] is None:
                info['__Output']['routeTick'] = 'Red'
                info['routeTick'] = '---'

            if info['route'] is not None:
                ready = 0
                for item in info['route']:
                    info['urlT'].append('http://%s' % (item['route']))
                    if item['ready']:
                        ready += 1

                if ready > 0 and ready == len(info['route']):
                    info['__Output']['routeTick'] = 'Green'
                else:
                    info['__Output']['routeTick'] = 'Red'

                info['routeTick'] = '%s/%s' % (ready, len(info['route']))

        info['credentials'] = {}
        if 'secret' in info and info['secret'] is not None:
            keys = [
                'hec_token',
                'idxc_secret',
                'pass4SymmKey',
                'password',
                'shc_secret'
            ]
            for key in keys:
                info['credentials'][key] = None
                key_mo = self.get(info['secret'], 'data:%s' % (key))
                if key_mo is not None:
                    info['credentials'][key] = base64.b64decode(
                        key_mo.encode('utf-8')
                    ).decode('utf-8')
            
            if info['credentials']['password'] is not None:
                info['urlT'].append('(admin, %s)' % (info['credentials']['password']))
                
        return info
    
    def get_splunk_standalones_info(self, cache_enabled=True):
        if cache_enabled:
            if self.splunk_standalone is not None:
                return self.splunk_standalone

        managed_objects = self.get_splunk_standalone_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.splunk_standalone = []
        for managed_object in managed_objects:
            splunk_standalone_info = {}
            splunk_standalone_info['info'] = self.get_splunk_standalone_info(
                managed_object
            )
            splunk_standalone_info['mo'] = managed_object
            self.splunk_standalone.append(
                splunk_standalone_info
            )

        return self.splunk_standalone

    def match_splunk_standalone(self, splunk_standalone_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, splunk_standalone_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (splunk_standalone_info['namespace'], splunk_standalone_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_splunk_standalone',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_splunk_standalones(self, object_filter=None, pod_info=False, pvc_info=False, service_info=False, route_info=False, secret_info=False, return_mo=False, cache_enabled=True):
        all_splunk_standalones = self.get_splunk_standalones_info(cache_enabled=cache_enabled)
        if all_splunk_standalones is None:
            return None

        splunk_standalones = []

        for splunk_standalone_info in all_splunk_standalones:
            if not self.match_splunk_standalone(splunk_standalone_info['info'], object_filter):
                continue

            if return_mo:
                splunk_standalones.append(
                    splunk_standalone_info['mo']
                )
                continue

            if pod_info:
                splunk_standalone_info['info']['pod'] = self.get_pod(
                    splunk_standalone_info['info']['namespace'],
                    'splunk-%s-standalone-0' % (splunk_standalone_info['info']['name'])
                )

            if service_info:
                splunk_standalone_info['info']['service'] = self.get_service(
                    splunk_standalone_info['info']['namespace'],
                    'splunk-%s-standalone-service' % (splunk_standalone_info['info']['name'])
                )

            if route_info:
                object_filter = []
                object_filter.append('namespace:%s' % (splunk_standalone_info['info']['namespace']))
                object_filter.append('service:splunk-%s-standalone-service' % (splunk_standalone_info['info']['name']))
                splunk_standalone_info['info']['route'] = self.get_routes(
                    object_filter=object_filter
                )

            if secret_info:
                splunk_standalone_info['info']['secret'] = self.get_secret(
                    splunk_standalone_info['info']['namespace'],
                    'splunk-%s-standalone-secret-v1' % (splunk_standalone_info['info']['name'])
                )

            if pvc_info:
                splunk_standalone_info['info']['pvc'] = []
                
                pvc = self.get_pvc(
                    splunk_standalone_info['info']['namespace'],
                    'pvc-etc-splunk-%s-standalone-0' % (splunk_standalone_info['info']['name'])
                )
                if pvc is not None:
                    splunk_standalone_info['info']['pvc'].append(pvc)

                pvc = self.get_pvc(
                    splunk_standalone_info['info']['namespace'],
                    'pvc-var-splunk-%s-standalone-0' % (splunk_standalone_info['info']['name'])
                )
                if pvc is not None:
                    splunk_standalone_info['info']['pvc'].append(pvc)

            splunk_standalone_info['info'] = self.get_splunk_standalone_extended_info(
                splunk_standalone_info['info']
            )

            splunk_standalones.append(
                splunk_standalone_info['info']
            )

        return splunk_standalones

    def get_splunk_standalone_names(self, cache_enabled=False):
        names = []
        standalones = self.get_splunk_standalones(cache_enabled=cache_enabled)
        if standalones is None:
            return None
        
        for standalone in standalones:
            names.append(
                dict(
                    namespace=standalone['namespace'],
                    name=standalone['name']
                )
            )

        return names

    def is_splunk_standalone(self, namespace, name, cache_enabled=True):
        if self.get_splunk_standalone(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_splunk_standalone(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        splunk_standalones = self.get_splunk_standalones(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if splunk_standalones is None:
            return None

        if len(splunk_standalones) == 1:
            return splunk_standalones[0]

        return None

    def get_splunk_standalone_body(self, namespace, name, pvc_finalizers=False):
        body = {}
        body['apiVersion'] = 'enterprise.splunk.com/v4'
        body['kind'] = 'Standalone'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name

        if pvc_finalizers:
            body['metadata']['finalizers'] = ['enterprise.splunk.com/delete-pvc']

        body['spec'] = {}
        return body

    def create_splunk_standalone(
            self, 
            namespace, 
            name, 
            pvc_finalizers=False,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Splunk Standalone Cluster', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            
        if self.is_splunk_standalone(namespace, name):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        body = self.get_splunk_standalone_body(
            namespace,
            name,
            pvc_finalizers=pvc_finalizers
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_splunk_standalone_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Standalone cluster created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        pod_namespace = namespace
        pod_name = 'splunk-%s-standalone-0' % (name)
        if my_output is not None:
            my_output.default('Wait for pod %s/%s...' % (pod_namespace, pod_name))
    
        if not self.wait_pod_phase(pod_namespace, pod_name, ['Running'], max_time=600):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for standalone ready %s/%s...' % (namespace, name))
    
        if not self.wait_splunk_standalone_ready(namespace, name):
            if my_output is not None:
                my_output.error('Timed out')
            return False
                
        return True    

    def wait_splunk_standalone_ready(self, namespace, name, max_time=300):
        start_time = int(time.time())
        while True:
            info = self.get_splunk_standalone(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_splunk_standalone_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def remove_splunk_standalone_finalizers(self, namespace, name):
        standalone_mo = self.get_splunk_standalone(namespace, name, return_mo=True, cache_enabled=False)
        if standalone_mo is None:
            return False
        
        modified = False
        if 'finalizers' in standalone_mo['spec']:
            del standalone_mo['spec']['finalizers']
            modified = True

        if 'finalizers' in standalone_mo['metadata']:
            del standalone_mo['metadata']['finalizers']
            modified = True

        if not modified:
            return True
        
        return self.replace_splunk_standalone_mo(standalone_mo)
    
    def delete_splunk_standalone(
            self, 
            namespace, 
            name,
            my_output=None, 
            wait=True,
            finalizers=True
        ):
        if my_output is not None:
            my_output.default('Delete Splunk Standalone Cluster', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            
        if not self.is_splunk_standalone(namespace, name):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_splunk_standalone_mo(namespace, name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Standalone cluster deleted', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if not wait:
            return True
        
        pod_namespace = namespace
        pod_name = 'splunk-%s-standalone-0' % (name)
        if my_output is not None:
            my_output.default('Wait for no pod %s/%s...' % (pod_namespace, pod_name))
    
        if not self.wait_no_pod(pod_namespace, pod_name, max_time=300):
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        if my_output is not None:
            my_output.default('Wait for no standalone %s/%s...' % (namespace, name))
    
        if not self.wait_no_splunk_standalone(namespace, name):
            if not finalizers:
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('Remove finalizers')

            if not self.remove_splunk_standalone_finalizers(namespace, name):
                if my_output is not None:
                    my_output.error('REST API failed')
                return False
            
            if not self.wait_no_splunk_standalone(namespace, name):
                if my_output is not None:
                    my_output.error('Giving up')
                return False
            
        return True    

    def wait_no_splunk_standalone(self, namespace, name, max_time=120):
        start_time = int(time.time())
        while True:
            info = self.get_splunk_standalone(
                namespace,
                name,
                cache_enabled=False
            )
            if info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_splunk_standalone',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)