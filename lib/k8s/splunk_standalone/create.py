class K8sSplunkStandaloneCreate():
    def __init__(self):
        pass

    def get_splunk_standalone_body(self, namespace, name, pvc_finalizers=False, etc_size=None, etc_sc=None, var_size=None, var_sc=None, sa='default'):
        body = {}
        body['apiVersion'] = 'enterprise.splunk.com/v4'
        body['kind'] = 'Standalone'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name

        if pvc_finalizers:
            body['metadata']['finalizers'] = ['enterprise.splunk.com/delete-pvc']

        body['spec'] = {}

        if etc_size is not None:
            body['spec']['etcVolumeStorageConfig'] = {}
            body['spec']['etcVolumeStorageConfig']['storageCapacity'] = etc_size
            if etc_sc is not None:
                body['spec']['etcVolumeStorageConfig']['storageClassName'] = etc_sc

        if var_size is not None:
            body['spec']['varVolumeStorageConfig'] = {}
            body['spec']['varVolumeStorageConfig']['storageCapacity'] = var_size
            if var_sc is not None:
                body['spec']['varVolumeStorageConfig']['storageClassName'] = var_sc

        if sa != 'default':
            body['spec']['serviceAccount'] = sa
            
        return body

    def create_splunk_standalone(
            self, 
            namespace, 
            name, 
            pvc_finalizers=False,
            etc_size='10Gi',
            etc_sc=None,
            var_size='100Gi',
            var_sc=None,
            sa='default',
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_splunk_standalone_body(
            namespace,
            name,
            pvc_finalizers=pvc_finalizers,
            etc_size=etc_size,
            etc_sc=etc_sc,
            var_size=var_size,
            var_sc=var_sc,
            sa=sa
        )

        success, _ = self.create_resource(body, object_name='splunk_standalone', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_pod_phase(
            namespace, 
            'splunk-%s-standalone-0' % (name), 
            ['Running'], 
            max_time=1800, 
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_splunk_standalone(
            namespace,
            name,
            match_properties={'ready':True},
            max_time=600,
            my_output=my_output
        )
        if not success:
            return False
                
        return True