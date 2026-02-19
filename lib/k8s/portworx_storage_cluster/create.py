import yaml
from menu.common import get_confirmation


class K8sPortworxStorageClusterCreate():
    def __init__(self):
        pass

    def get_portworx_storage_cluster_definition(
            self, 
            namespace, 
            name,
            cert=False,
            tls=False,
            diags=False
        ):
        body = {}
        body['apiVersion'] = 'core.libopenstorage.org/v1'
        body['kind'] = 'StorageCluster'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name

        body['annotations'] = []
        annotation = {}
        annotation['portworx.io/is-openshift'] = 'true'
        body['annotations'].append(annotation)

        body['spec'] = {}
        body['spec']['certManager'] = {}
        body['spec']['certManager']['enabled'] = cert
        body['spec']['kvdb'] = {}
        body['spec']['kvdb']['enableTLS'] = tls
        body['spec']['clusterDiags'] = {}
        body['spec']['clusterDiags']['enabled'] = diags

        return body
    
    def create_portworx_storage_cluster(
            self, 
            namespace='openshift-operators', 
            name='portworx', 
            body=None, 
            cert=False,
            tls=False,
            diags=False,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Portworx Storage Cluster', before_newline=True, underline=True)

        if self.is_portworx_storage_cluster():
            if my_output is not None:
                my_output.default('- already exists')
            return True

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
            body = self.get_portworx_storage_cluster_definition(
                namespace,
                name,
                cert=cert,
                tls=tls,
                diags=diags,
            )

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_portworx_storage_cluster_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        # if my_output is not None:
        #     my_output.default('Wait until ready or degraded [timeout:180s]...')

        # success = self.wait_portworx_storage_cluster_states(['Ready', 'Degraded'], max_time=180)
        # if not success:
        #     if my_output is not None:
        #         my_output.error('Timed out')
                
        #     return False

        # if my_output is not None:
        #     my_output.default('Wait for portworx_storage storage class [timeout:180s]...')

        # if not self.wait_storage_class_portworx_storage(max_time=180):
        #     if my_output is not None:
        #         my_output.error('Timed out')
        #     return False

        return True
