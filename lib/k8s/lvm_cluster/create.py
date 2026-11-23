import yaml
from menu.common import get_confirmation


class K8sLvmClusterCreate():
    def __init__(self):
        pass

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

        success, _ = self.create_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until ready [timeout:600s]...')

        success = self.wait_lvm_cluster_states(['Ready'], max_time=600)
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