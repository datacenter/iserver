class K8sPodDelete():
    def __init__(self):
        pass
    
    def delete_pod(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Pod', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        if not self.is_pod(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_pod_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no pod')

        success = self.wait_no_pod(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True

    def delete_pods(self, object_filter, confirmation=False, my_output=None, k8s_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete PODs', before_newline=True, underline=True)
            my_output.default('Object filter', before_newline=True)
            for item in object_filter:
                my_output.default('- %s' % (item))

        pods = self.get_pods(
            object_filter=object_filter,
            cache_enabled=False
        )
        if pods is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if k8s_output is not None:
            k8s_output.print_pods_state(pods)
        
        if confirmation:
            if not get_confirmation():
                return False
            
        if my_output is not None:
            my_output.default('Delete', before_newline=True)

        for pod in pods:
            my_output.default('- %s' % (pod['name']))
            success = self.delete_pod_mo(pod['namespace'], pod['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')
                continue

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no pod...')

                if not self.wait_no_pod(pod['namespace'], pod['name']):
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False
                    
        return True
