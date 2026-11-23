class K8sPodCreate():
    def __init__(self):
        pass
    
    def create_pod(
            self, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        success, created = self.create_resource(body, object_name='pod', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        if not created:
            return True
        
        if not wait:
            return True
        
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')
        
        success = self.wait_pod_phase(namespace, name, 'Running', max_time=600, my_output=my_output)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        return True
