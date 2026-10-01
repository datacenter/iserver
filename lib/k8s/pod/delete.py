from menu.common import get_confirmation


class K8sPodDelete():
    def __init__(self):
        pass
    
    def delete_pod(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'Pod', 
            'v1',
            name, 
            'pod',
            namespace=namespace,
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success

    def delete_pods(self, object_filter, confirmation=False, my_output=None, k8s_output=None, wait=True):
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

        success = True
        for pod in pods:
            pod_success = self.delete_pod(
                pod['namespace'], 
                pod['name'], 
                my_output=my_output, 
                wait=wait
            )
            success = success and pod_success

        return success