from lib import filter_helper


class K8sDeploymentOauth():
    def __init__(self):
        pass

    def is_deployment_oauth(self, deployment):
        if 'metadata' in deployment:
            labels_mo = filter_helper.get(deployment, 'metadata:labels')
            if labels_mo is not None:
                if 'app' in labels_mo:
                    if labels_mo['app'] == 'oauth-openshift':
                        return True
                    
        if 'metadata' not in deployment:
            if 'app' in deployment['label']:
                if deployment['label']['app'] == 'oauth-openshift':
                    return True
                            
        return False
    
    def get_oauth_deployments(self, namespace='openshift-authentication', return_mo=False, cache_enabled=True):
        deployments = self.get_deployments(
            object_filter=['namespace:%s' % (namespace)],
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if deployments is None:
            return None
        
        oauth_deployments = []
        for deployment in deployments:
            if not self.is_deployment_oauth(deployment=deployment):
                continue
            oauth_deployments.append(deployment)

        return oauth_deployments

    def is_deployment_oauth_operator(self, deployment):
        if 'metadata' in deployment:
            labels_mo = filter_helper.get(deployment, 'metadata:labels')
            if labels_mo is not None:
                if 'app' in labels_mo:
                    if labels_mo['app'] == 'authentication-operator':
                        return True
                    
        if 'metadata' not in deployment:
            if 'app' in deployment['label']:
                if deployment['label']['app'] == 'authentication-operator':
                    return True
                            
        return False
    
    def get_oauth_operator_deployments(self, namespace='openshift-authentication-operator', return_mo=False, cache_enabled=True):
        deployments = self.get_deployments(
            object_filter=['namespace:%s' % (namespace)],
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if deployments is None:
            return None
        
        oauth_deployments = []
        for deployment in deployments:
            if not self.is_deployment_oauth_operator(deployment=deployment):
                continue
            oauth_deployments.append(deployment)

        return oauth_deployments
        
    def wait_oauth_deployments_restart(self, deployments, my_output=None):
        if my_output is not None:
            my_output.default('OAuth restart', before_newline=True)

        success = self.wait_no_deployments(deployments, my_output=my_output, max_time=180)
        if not success:
            if my_output is not None:
                my_output.default('- oauth deployments did not restart (possible reason no-configuration-change)')
            return True
        
        prompt = '- wait for deployment openshift-authentication/oauth-openshift ready state [timeout:180s]'
        success = self.wait_deployment_ready_state('openshift-authentication', 'oauth-openshift', my_output=my_output, prompt=prompt, max_time=180)
        return success
    