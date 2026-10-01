class K8sSplunkStandaloneCreate():
    def __init__(self):
        pass

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
        body = self.get_splunk_standalone_body(
            namespace,
            name,
            pvc_finalizers=pvc_finalizers
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