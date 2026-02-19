import yaml
import time
from lib import filter_helper
from menu.common import get_confirmation


class K8sLvmClusterInfo():
    def __init__(self):
        self.lvm_cluster = None

    def get_lvm_cluster_info(self, lvm_cluster_mo):
        if lvm_cluster_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            lvm_cluster_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(lvm_cluster_mo, 'spec')
        info['status'] = self.get(lvm_cluster_mo, 'status')

        info['info'] = {}

        info['info']['state'] = self.get(lvm_cluster_mo, 'status:state')
        info['info']['ready'] = self.get(lvm_cluster_mo, 'status:ready', on_error=False, on_none=False)
        if info['info']['ready']:
            info['info']['readyTick'] = '\u2713'
            info['__Output']['info.readyTick'] = 'Green'
        else:
            info['info']['readyTick'] = '\u2717'
            info['__Output']['info.readyTick'] = 'Red'

        info['info']['resourcesAvailable'] = False
        info['info']['resourcesAvailableReason'] = None
        info['info']['resourcesAvailableMessage'] = None
        info['info']['resourcesAvailableDescription'] = None

        info['info']['vgsReady'] = False
        info['info']['vgsReadyReason'] = None
        info['info']['vgsReadyMessage'] = None
        info['info']['vgsReadyDescription'] = None

        conditions_mo = self.get(lvm_cluster_mo, 'status:conditions', on_error=[], on_none=[])
        for condition_mo in conditions_mo:
            contition_type = self.get(condition_mo, 'type', on_error="N/A", on_none="N/A")
            condition_status = self.get(condition_mo, 'status', on_error='False', on_none='False')
            if contition_type == 'ResourcesAvailable':
                if condition_status == 'True':
                    info['info']['resourcesAvailable'] = True

                info['info']['resourcesAvailableReason'] = self.get(condition_mo, 'reason')
                info['info']['resourcesAvailableMessage'] = self.get(condition_mo, 'message')
                info['info']['resourcesAvailableDescription'] = '[%s] %s' % (
                    info['info']['resourcesAvailableReason'],
                    info['info']['resourcesAvailableMessage']
                )

            if contition_type == 'VolumeGroupsReady':
                if condition_status == 'True':
                    info['info']['vgsReady'] = True

                info['info']['vgsReadyReason'] = self.get(condition_mo, 'reason')
                info['info']['vgsReadyMessage'] = self.get(condition_mo, 'message')
                info['info']['vgsReadyDescription'] = '[%s] %s' % (
                    info['info']['vgsReadyReason'],
                    info['info']['vgsReadyMessage']
                )

        if info['info']['resourcesAvailable']:
            info['info']['resourcesAvailableTick'] = '\u2713'
            info['__Output']['info.resourcesAvailableTick'] = 'Green'
        else:
            info['info']['resourcesAvailableTick'] = '\u2717'
            info['__Output']['info.resourcesAvailableTick'] = 'Red'

        if info['info']['vgsReady']:
            info['info']['vgsReadyTick'] = '\u2713'
            info['__Output']['info.vgsReadyTick'] = 'Green'
        else:
            info['info']['vgsReadyTick'] = '\u2717'
            info['__Output']['info.vgsReadyTick'] = 'Red'

        info['info']['deviceClass'] = []

        device_classes_mo = self.get(lvm_cluster_mo, 'spec:storage:deviceClasses', on_error=[], on_none=[])
        device_classes_status_mo = self.get(lvm_cluster_mo, 'status:deviceClassStatuses', on_error=[], on_none=[])
        for device_class_mo in device_classes_mo:
            device_class_info = {}
            device_class_info['__Output'] = {}
            device_class_info['name'] = self.get(device_class_mo, 'name')
            device_class_info['fstype'] = self.get(device_class_mo, 'fstype')
            device_class_info['default'] = self.get(device_class_mo, 'default', on_error=False, on_none=False)
            if device_class_info['default']:
                device_class_info['defaultTick'] = '\u2713'
                device_class_info['__Output']['defaultTick'] = 'Green'
            else:
                device_class_info['defaultTick'] = '\u2717'
                device_class_info['__Output']['defaultTick'] = 'Red'

            device_class_info['nodeSelector'] = self.get(device_class_mo, 'nodeSelector')
            device_class_info['deviceSelector'] = self.get(device_class_mo, 'deviceSelector')
            device_class_info['thinPoolConfig'] = self.get(device_class_mo, 'thinPoolConfig')

            device_class_info['nodesCount'] = 0
            device_class_info['nodesReady'] = 0

            device_class_info['nodeStatus'] = []
            for device_class_status_mo in device_classes_status_mo:
                if device_class_status_mo['name'] == device_class_info['name']:
                    device_class_info['nodeStatus'] = self.get(device_class_status_mo, 'nodeStatus', on_error=[], on_none=[])
                    for node_status in device_class_info['nodeStatus']:
                        device_class_info['nodesCount'] += 1
                        node_status['__Output'] = {}
                        excluded_mo = self.get(node_status, 'excluded', on_error=[], on_none=[])
                        node_status['excludedDevices'] = []
                        node_status['excludedReasons'] = []
                        node_status['excludedCount'] = len(
                            excluded_mo
                        )
                        for excluded in excluded_mo:
                            node_status['excludedDevices'].append(
                                excluded['name']
                            )
                            for reason in excluded['reasons']:
                                node_status['excludedReasons'].append(reason)

                        if node_status['status'] == 'Ready':
                            node_status['__Output']['status'] = 'Green'
                            node_status['ready'] = True
                            device_class_info['nodesReady'] += 1
                        else:
                            node_status['__Output']['status'] = 'Red'
                            node_status['ready'] = False

            device_class_info['nodesSummary'] = '%s/%s' % (
                device_class_info['nodesReady'],
                device_class_info['nodesCount']
            )
            if device_class_info['nodesReady'] == device_class_info['nodesCount'] and device_class_info['nodesCount'] > 0:
                device_class_info['__Output']['nodesSummary'] = 'Green'
            else:
                device_class_info['__Output']['nodesSummary'] = 'Red'

            info['info']['deviceClass'].append(
                device_class_info
            )

        info['info']['deviceClass'] = sorted(
            info['info']['deviceClass'],
            key=lambda i: i['name']
        )
        return info

    def get_lvm_clusters_info(self, cache_enabled=True):
        if cache_enabled:
            if self.lvm_cluster is not None:
                return self.lvm_cluster

        managed_objects = self.get_lvm_cluster_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.lvm_cluster = []
        for managed_object in managed_objects:
            lvm_cluster_info = {}
            lvm_cluster_info['info'] = self.get_lvm_cluster_info(
                managed_object
            )
            lvm_cluster_info['mo'] = managed_object
            self.lvm_cluster.append(
                lvm_cluster_info
            )

        return self.lvm_cluster

    def match_lvm_cluster(self, lvm_cluster_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, lvm_cluster_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, lvm_cluster_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_lvm_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_lvm_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_lvm_clusters = self.get_lvm_clusters_info(cache_enabled=cache_enabled)
        if all_lvm_clusters is None:
            return None

        lvm_clusters = []

        for lvm_cluster_info in all_lvm_clusters:
            if not self.match_lvm_cluster(lvm_cluster_info['info'], object_filter):
                continue

            if return_mo:
                lvm_clusters.append(
                    lvm_cluster_info['mo']
                )
                continue

            lvm_clusters.append(
                lvm_cluster_info['info']
            )

        return lvm_clusters

    def is_lvm_cluster(self, cache_enabled=True):
        if self.get_lvm_cluster(cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_lvm_cluster_ready(self, cache_enabled=True):
        lvm_cluster = self.get_lvm_cluster(cache_enabled=cache_enabled)
        if lvm_cluster is None:
            return False
        
        return lvm_cluster['info']['ready']

    def get_lvm_cluster_state(self, cache_enabled=True):
        cluster_info = self.get_lvm_cluster(cache_enabled=cache_enabled)
        if cluster_info is None:
            return None
        return cluster_info['info']['state']

    def get_lvm_cluster(self, return_mo=False, cache_enabled=True):
        object_filter = []
        lvm_clusters = self.get_lvm_clusters(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if lvm_clusters is None:
            return None

        if len(lvm_clusters) == 1:
            return lvm_clusters[0]

        return None

    def wait_lvm_cluster_ready(self, max_time=180):
        start_time = int(time.time())
        while True:
            if self.is_lvm_cluster_ready(cache_enabled=False):
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_lvm_cluster_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_lvm_cluster_states(self, states, max_time=180):
        start_time = int(time.time())
        while True:
            state = self.get_lvm_cluster_state(cache_enabled=False)
            if state is not None:
                if state in states:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_lvm_cluster_states',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_lvm_cluster(self, max_time=60):
        start_time = int(time.time())
        while True:
            lvm_cluster_info = self.get_lvm_cluster(
                cache_enabled=False
            )
            if lvm_cluster_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_lvm_cluster',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def get_lvm_cluster_definition(
            self, 
            namespace, 
            name, 
            vg_name, 
            pool_name, 
            default_storage_class=False,
            devices=None,
            chunk_size=None
        ):
        body = {}
        body['apiVersion'] = 'lvm.topolvm.io/v1alpha1'
        body['kind'] = 'LVMCluster'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['storage'] = {}

        device_class = {}
        device_class['fstype'] = 'xfs'
        device_class['default'] = default_storage_class
        device_class['name'] = vg_name
        device_class['thinPoolConfig'] = {}
        device_class['thinPoolConfig']['chunkSizeCalculationPolicy'] = 'Static'
        device_class['thinPoolConfig']['metadataSizeCalculationPolicy'] = 'Host'
        device_class['thinPoolConfig']['sizePercent'] = 90
        device_class['thinPoolConfig']['name'] = pool_name
        device_class['thinPoolConfig']['overprovisionRatio'] = 10

        if chunk_size is not None:
            device_class['thinPoolConfig']['chunkSize'] = chunk_size
            
        if devices is not None and len(devices) > 0:
            device_class['deviceSelector'] = {}
            device_class['deviceSelector']['paths'] = devices
            
        body['spec']['storage']['deviceClasses'] = [device_class]

        return body
    
    def create_lvm_cluster(
            self, 
            namespace='openshift-storage', 
            name='lvmcluster', 
            vg_name='vg1', 
            pool_name='thin-pool-1', 
            default_storage_class=False,
            devices=None, 
            chunk_size=None,
            body=None, 
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create LVM Cluster', before_newline=True, underline=True)

        if self.is_lvm_cluster():
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if self.get_storage_class_lvm(cache_enabled=False) is not None:
            if my_output is not None:
                my_output.error('LVM Cluster storage class already exists')
            return False

        if body is not None:
            try:
                namespace = body['metadata']['namespace']
                name = body['metadata']['name']
            except BaseException:
                if my_output is not None:
                    my_output.error('Invalid body format')
                return False
            
        if my_output is not None:
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if body is None:
            body = self.get_lvm_cluster_definition(
                namespace,
                name,
                vg_name,
                pool_name,
                default_storage_class=default_storage_class,
                devices=devices,
                chunk_size=chunk_size
            )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_lvm_cluster_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until ready or degraded [timeout:180s]...')

        success = self.wait_lvm_cluster_states(['Ready', 'Degraded'], max_time=180)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
                
            return False

        if my_output is not None:
            my_output.default('Wait for lvm storage class [timeout:180s]...')

        if not self.wait_storage_class_lvm(max_time=180):
            if my_output is not None:
                my_output.error('Timed out')
            return False

        return True

    def remove_lvm_cluster_finalizers(self):
        cluster_mo = self.get_lvm_cluster(return_mo=True, cache_enabled=False)
        if cluster_mo is None:
            return False
        
        if 'finalizers' not in cluster_mo['metadata']:
            return True
        
        del cluster_mo['metadata']['finalizers']

        return self.set_lvm_cluster_mo(cluster_mo)
    
    def delete_lvm_cluster(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete LVM Cluster', before_newline=True, underline=True)

        info = self.get_lvm_cluster(cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if my_output is not None:
            my_output.default('- namespace: %s' % (info['namespace']))
            my_output.default('- name: %s' % (info['name']))
        
        if not self.delete_lvm_cluster_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete lvm cluster')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no lvm cluster')

            if not self.wait_no_lvm_cluster():
                if my_output is not None:
                    my_output.default('LVM Cluster instance still there... checking finalizers...')

                if not self.remove_lvm_cluster_finalizers():
                    if my_output is not None:
                        my_output.error('Finalizers update failed')
                    return False
                
                if my_output is not None:
                    my_output.default('Finalizers removed')
                    my_output.default('Wait for no lvm cluster [timeout:60s]...')

                success = self.wait_no_lvm_cluster(max_time=60)
                if not success:
                    if my_output is not None:
                        my_output.error('Giving up')
                    return False
            
        return True
