from lib import filter_helper


class K8sPodOauth():
    def __init__(self):
        pass

    def is_pod_oauth(self, pod):
        if 'metadata' in pod:
            labels_mo = filter_helper.get(pod, 'metadata:labels')
            if labels_mo is not None:
                if 'app' in labels_mo:
                    if labels_mo['app'] == 'oauth-openshift':
                        return True
                    
        if 'metadata' not in pod:
            if 'app' in pod['label']:
                if pod['label']['app'] == 'oauth-openshift':
                    return True
                            
        return False
    
    def get_oauth_pods(self, namespace='openshift-authentication', return_mo=False, cache_enabled=True):
        pods = self.get_pods(
            namespace=namespace,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if pods is None:
            return None
        
        oauth_pods = []
        for pod in pods:
            if not self.is_pod_oauth(pod=pod):
                continue
            oauth_pods.append(pod)

        return oauth_pods
    
    def wait_oauth_pods_restart(self, pods, my_output=None):
        if my_output is not None:
            my_output.default('OAuth restart', before_newline=True)

        success = self.wait_no_pods(pods, my_output=my_output, max_time=180)
        if not success:
            if my_output is not None:
                my_output.default('- oauth pods did not restart (possible reason no-configuration-change)')
            return True
        
        prompt = '- wait for deployment openshift-authentication/oauth-openshift ready state [timeout:180s]'
        success = self.wait_deployment_ready_state('openshift-authentication', 'oauth-openshift', my_output=my_output, prompt=prompt, max_time=180)
        return success
    