import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sPortworxStorageNodeInfo():
    def __init__(self):
        self.portworx_storage_node = None

    def get_portworx_storage_node_info(self, portworx_storage_node_mo):
        if portworx_storage_node_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            portworx_storage_node_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(portworx_storage_node_mo, 'spec')
        info['status'] = self.get(portworx_storage_node_mo, 'status')

        info['local_storage_sc'] = None
        info['storage_class'] = None
        devices_mo = self.get(portworx_storage_node_mo, 'spec:storageDeviceSets', on_error=[], on_none=[])
        for device_mo in devices_mo:
            info['local_storage_sc'] = self.get(device_mo, 'dataPVCTemplate:spec:storageClassName')
            info['storage_class'] = self.get(device_mo, 'name')

        info['phase'] = self.get(portworx_storage_node_mo, 'status:phase')
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

        info['hostnames'] = self.get(portworx_storage_node_mo, 'status:nodeTopologies:labels:kubernetes.io/hostname', on_error=[], on_none=[])
        if len(info['hostnames']) == 0:
            info['hostnamesT'] = '--'
        else:
            info['hostnamesT'] = ', '.join(info['hostnames'])
        
        info['version'] = self.get(portworx_storage_node_mo, 'status:version')
        info['current_mon_count'] = self.get(portworx_storage_node_mo, 'status:currentMonCount')
        info['expected_osd_count'] = None
        device_sets_mo = self.get(portworx_storage_node_mo, 'spec:storageDeviceSets')
        if device_sets_mo is not None and len(device_sets_mo) == 1:
            try:
                info['expected_osd_count'] = self.get(device_sets_mo[0], 'replica') * self.get(device_sets_mo[0], 'count')
            except BaseException:
                pass

        return info

    def get_portworx_storage_nodes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.portworx_storage_node is not None:
                return self.portworx_storage_node

        managed_objects = self.get_portworx_storage_node_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.portworx_storage_node = []
        for managed_object in managed_objects:
            portworx_storage_node_info = {}
            portworx_storage_node_info['info'] = self.get_portworx_storage_node_info(
                managed_object
            )
            portworx_storage_node_info['mo'] = managed_object
            self.portworx_storage_node.append(
                portworx_storage_node_info
            )

        return self.portworx_storage_node

    def match_portworx_storage_node(self, portworx_storage_node_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, portworx_storage_node_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, portworx_storage_node_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_portworx_storage_node',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_portworx_storage_nodes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_portworx_storage_nodes = self.get_portworx_storage_nodes_info(cache_enabled=cache_enabled)
        if all_portworx_storage_nodes is None:
            return None

        portworx_storage_nodes = []

        for portworx_storage_node_info in all_portworx_storage_nodes:
            if not self.match_portworx_storage_node(portworx_storage_node_info['info'], object_filter):
                continue

            if return_mo:
                portworx_storage_nodes.append(
                    portworx_storage_node_info['mo']
                )
                continue

            portworx_storage_nodes.append(
                portworx_storage_node_info['info']
            )

        return portworx_storage_nodes

    def is_portworx_storage_node(self, cache_enabled=True):
        if self.get_portworx_storage_node(cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_portworx_storage_node(self, return_mo=False, cache_enabled=True):
        portworx_storage_nodes = self.get_portworx_storage_nodes(
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if portworx_storage_nodes is None:
            return None

        if len(portworx_storage_nodes) == 1:
            return portworx_storage_nodes[0]

        return None

    def get_portworx_storage_node_body(
            self, 
            namespace,
            name,
            storage_class,
            local_storage_sc,
            count,
            replica,
            default_sc=False,
            default_virt_sc=False,
            flexible_scaling=True,
            nfs=False,
            tools=False
        ):
        body = {}
        body['apiVersion'] = 'ocs.openshift.io/v1'
        body['kind'] = 'StorageNode'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}

        body['spec']['arbiter'] = {}
        body['spec']['encryption'] = {}
        body['spec']['encryption']['kms'] = {}
        body['spec']['encryption']['keyRotation'] = dict(schedule='@weekly')
        body['spec']['externalStorage'] = {}
        body['spec']['flexibleScaling'] = flexible_scaling
        body['spec']['managedResources'] = {}
        body['spec']['managedResources']['cephBlockPools'] = dict(
            defaultStorageClass=default_sc,
            defaultVirtualizationStorageClass=default_virt_sc
        )
        body['spec']['managedResources']['cephCluster'] = {}
        body['spec']['managedResources']['cephConfig'] = {}
        body['spec']['managedResources']['cephDashboard'] = {}
        body['spec']['managedResources']['cephFilesystems'] = {}
        body['spec']['managedResources']['cephNonResilientPools'] = {}
        body['spec']['managedResources']['cephObjectStoreUsers'] = {}
        body['spec']['managedResources']['cephObjectStores'] = {}
        body['spec']['managedResources']['cephRBDMirror'] = {}
        body['spec']['managedResources']['cephToolbox'] = {}
        body['spec']['monDataDirHostPath'] = '/var/lib/rook'
        body['spec']['nfs'] = dict(enable=nfs)
        body['spec']['nfnodeTopologies'] = {}

        device_set_mo = {}
        device_set_mo['name'] = storage_class
        device_set_mo['count'] = count
        device_set_mo['replica'] = replica
        device_set_mo['config'] = {}
        device_set_mo['placement'] = {}
        device_set_mo['preparePlacement'] = {}
        device_set_mo['resources'] = {}
        device_set_mo['dataPVCTemplate'] = {}
        device_set_mo['dataPVCTemplate']['metadata'] = {}
        device_set_mo['dataPVCTemplate']['spec'] = {}
        device_set_mo['dataPVCTemplate']['spec']['accessModes'] = ['ReadWriteOnce']
        device_set_mo['dataPVCTemplate']['spec']['resources'] = {}
        device_set_mo['dataPVCTemplate']['spec']['resources']['requests'] = dict(storage='1')
        device_set_mo['dataPVCTemplate']['spec']['storageClassName'] = local_storage_sc
        device_set_mo['dataPVCTemplate']['spec']['volumeMode'] = 'Block'
        device_set_mo['dataPVCTemplate']['status'] = {}
        body['spec']['storageDeviceSets'] = [device_set_mo]

        if tools:
            body['spec']['enableCephTools'] = True
        
        return body

    def create_portworx_storage_node_from_params(
            self, 
            namespace,
            name,
            storage_class,
            local_storage_sc,
            count,
            replica,
            default_sc=False,
            default_virt_sc=False,
            flexible_scaling=True,
            nfs=False,
            tools=False,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Storage Cluster', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- storage class: %s' % (storage_class))
            my_output.default('- default storage class: %s' % (default_sc))
            my_output.default('- default virtualization storage class: %s' % (default_virt_sc))
            my_output.default('- nfs: %s' % (nfs))
            my_output.default('- lso storage class: %s' % (local_storage_sc))
            my_output.default('- replica: %s' % (replica))
            my_output.default('- count: %s' % (count))
            my_output.default('- flexible scaling: %s' % (flexible_scaling))
            my_output.default('- ceph tools: %s' % (tools))
        
        if self.is_portworx_storage_node(cache_enabled=False):
            if my_output is not None:
                my_output.default('- storage cluster already defined')
            return True
        
        body = self.get_portworx_storage_node_body(
            namespace,
            name,
            storage_class,
            local_storage_sc,
            count,
            replica,
            default_sc=default_sc,
            default_virt_sc=default_virt_sc,
            flexible_scaling=flexible_scaling,
            nfs=nfs,
            tools=tools
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_portworx_storage_node_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- storage cluster created', before_newline=True, after_newline=True)
    
        if wait:
            if my_output is not None:
                my_output.default('- wait for storage cluster crd...')
            
            success = self.wait_portworx_storage_node()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('- wait for ceph cluster crd...')
            
            success = self.wait_ceph_cluster()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                    
            if my_output is not None:
                my_output.default('- wait for storage cluster resources...')

            if not self.wait_odf_cluster_resources(my_output=my_output):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('- wait for storage cluster crd...')
            
            success = self.wait_portworx_storage_node_ready()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                                
        return True

    def create_portworx_storage_node_from_body(
            self, 
            namespace,
            name,
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Storage Cluster', before_newline=True, underline=True)
        
        if self.is_portworx_storage_node(cache_enabled=False):
            if my_output is not None:
                my_output.default('- storage cluster already defined')
            return True

        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_portworx_storage_node_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- storage cluster created', before_newline=True, after_newline=True)
    
        if wait:
            if my_output is not None:
                my_output.default('- wait for storage cluster crd...')
            
            success = self.wait_portworx_storage_node()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if my_output is not None:
                my_output.default('- wait for ceph cluster crd...')
            
            success = self.wait_ceph_cluster()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
        
            if my_output is not None:
                my_output.default('- wait for storage cluster resources...')

            if not self.wait_odf_cluster_resources(my_output=my_output):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('- wait for storage cluster crd...')
            
            success = self.wait_portworx_storage_node_ready()
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                                
        return True

    def wait_portworx_storage_node(self, max_time=360):
        start_time = int(time.time())
        while True:
            portworx_storage_node_info = self.get_portworx_storage_node(
                cache_enabled=False
            )
            if portworx_storage_node_info is not None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_node',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_portworx_storage_node_ready(self, max_time=360):
        start_time = int(time.time())
        while True:
            portworx_storage_node_info = self.get_portworx_storage_node(
                cache_enabled=False
            )
            if portworx_storage_node_info is not None:
                if portworx_storage_node_info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_node_ready',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def get_odf_cluster_resource_names(self, my_output=None):
        ceph_cluster = self.get_ceph_cluster(cache_enabled=False)
        if ceph_cluster is None:
            if my_output is not None:
                my_output.error('Ceph cluster object not found')
            return None

        if ceph_cluster['monitor_count'] is None:
            if my_output is not None:
                my_output.error('Failed to get expected monitor count')
            return None

        if ceph_cluster['manager_count'] is None:
            if my_output is not None:
                my_output.error('Failed to get expected manager count')
            return None

        portworx_storage_node = self.get_portworx_storage_node(cache_enabled=False)
        if portworx_storage_node is None:
            if my_output is not None:
                my_output.error('Storage cluster object not found')
            return None

        if portworx_storage_node['expected_osd_count'] is None:
            if my_output is not None:
                my_output.error('Failed to get expected osd count')
            return None

        nodes = self.get_nodes(
            object_filter=['label:cluster.ocs.openshift.io/openshift-storage'],
            cache_enabled=False
        )
        if nodes is None:
            if my_output is not None:
                my_output.error('Failed to get nodes')
            return None

        if len(nodes) == 0:
            if my_output is not None:
                my_output.error('No nodes with label: cluster.ocs.openshift.io/openshift-storage')
            return None

        deployments = [
            {'namespace': 'openshift-storage', 'name': 'csi-rbdplugin-provisioner'},
            {'namespace': 'openshift-storage', 'name': 'csi-cephfsplugin-provisioner'},
            {'namespace': 'openshift-storage', 'name': 'noobaa-endpoint'},
            {'namespace': 'openshift-storage', 'name': 'ocs-metrics-exporter'}
        ]

        monitor_names = ['rook-ceph-mon-a', 'rook-ceph-mon-b', 'rook-ceph-mon-c']
        for index in range(0, ceph_cluster['monitor_count']):
            deployments.append(
                dict(
                    namespace='openshift-storage',
                    name=monitor_names[index]
                )
            )
        
        manager_names = ['rook-ceph-mgr-a', 'rook-ceph-mgr-b']
        for index in range(0, ceph_cluster['manager_count']):
            deployments.append(
                dict(
                    namespace='openshift-storage',
                    name=manager_names[index]
                )
            )
        
        for index in range(0, portworx_storage_node['expected_osd_count']):
            deployments.append(
                dict(
                    namespace='openshift-storage',
                    name='rook-ceph-osd-%s' % (index)
                )
            )

        for node in nodes:
            deployments.append(
                dict(
                    namespace='openshift-storage',
                    name='rook-ceph-crashcollector-%s' % (node['name'])
                )
            )
            deployments.append(
                dict(
                    namespace='openshift-storage',
                    name='rook-ceph-exporter-%s' % (node['name'])
                )
            )

        return deployments
    
    def wait_odf_cluster_resources(self, my_output=None, max_time=3600):
        deployments = self.get_odf_cluster_resource_names(my_output=my_output)
        if deployments is None:
            return False
        
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, max_time=3600, optional=False, allow_zero_replicas=True)
        if not success:
            return False

        return True

    def delete_portworx_storage_node(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete storage cluster', before_newline=True, underline=True)

        info = self.get_portworx_storage_node(cache_enabled=False)
        if info is None:
            my_output.default('- already deleted')
            return True
        
        if not self.delete_portworx_storage_node_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('- rest api successful')
        
        if wait:
            if my_output is not None:
                my_output.default('- wait for no storage cluster resources...')

            if not self.wait_no_odf_cluster():
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            if my_output is not None:
                my_output.default('- wait for no storage cluster crd [timeout:60]...')

            if not self.wait_no_portworx_storage_node():
                if my_output is not None:
                    my_output.error('Timed out')
                return False
                    
        return True

    def wait_no_portworx_storage_node(self, max_time=60):
        start_time = int(time.time())
        while True:
            portworx_storage_node_info = self.get_portworx_storage_node(
                cache_enabled=False
            )
            if portworx_storage_node_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_portworx_storage_node',
                    'Max time reached'
                )
                return False

            time.sleep(5)

    def wait_no_odf_cluster(self, my_output=None):
        deployments = self.get_odf_cluster_resource_names(my_output=my_output)
        if deployments is None:
            return False

        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True