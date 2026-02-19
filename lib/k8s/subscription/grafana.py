import time


class K8sSubscriptionGrafana():
    def __init__(self):
        pass

    def is_grafana_subscription(self, namespace, name):
        return self.is_subscription(namespace, name, cache_enabled=False)

    def create_grafana_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic',
            name,
            'community-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation,
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            info = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                success = self.wait_subscription_grafana_ready(namespace, info['channel'], my_output=my_output)
                if not success:
                    return False
        
        return True

    def delete_grafana_subscription(self, namespace, name, my_output=None, wait=True):
        info = self.get_subscription(
            namespace,
            name,
            cache_enabled=False
        )

        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait and info is not None:
            success = self.wait_no_subscription_grafana(namespace, info['channel'], my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def wait_subscription_grafana_ready(self, namespace, channel, my_output=None):
        deployments = [
            {'namespace': namespace, 'name': 'grafana-operator-controller-manager-%s' % (channel)}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=True)
        if not success:
            return False

        return True

    def wait_no_subscription_grafana(self, namespace, channel, my_output=None):
        deployments = [
            {'namespace': namespace, 'name': 'grafana-operator-controller-manager-%s' % (channel)}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True
    