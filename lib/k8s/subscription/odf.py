import time


class K8sSubscriptionOdf():
    def __init__(self):
        pass

    def get_ocs_operator_subscription(self, name='ocs-operator', csv_info=False, deployment_info=False, replica_set_info=False, cache_enabled=True):
        info = self.get_subscription_by_package(
            name,
            csv_info=csv_info,
            cache_enabled=cache_enabled
        )
        if info is None:
            return None
        
        if deployment_info:
            info['deployment'] = self.get_deployment('openshift-storage', 'ocs-operator', cache_enabled=cache_enabled)

        if replica_set_info:
            info['replica_set'] = self.get_replica_set_deployment('openshift-storage', 'ocs-operator', cache_enabled=cache_enabled)
            
        return info
    
    def is_odf_subscription(self, namespace, name, cache_enabled=True):
        return self.is_subscription(namespace, name, cache_enabled=cache_enabled)

    def create_odf_subscription(self, namespace, name, channel, confirmation=False, my_output=None, wait=True):
        success = self.create_subscription(
            namespace, 
            name, 
            'Automatic', 
            name, 
            'redhat-operators', 
            'openshift-marketplace', 
            channel=channel,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )
        if not success:
            return False
        
        if wait:
            success = self.wait_subscription_odf_ready(my_output=my_output)
            if not success:
                return False
        
        return True
    
    def delete_odf_subscription(self, namespace, name, my_output=None, wait=True):
        success = self.delete_subscription(
            namespace, 
            name, 
            my_output=my_output, 
            wait=wait
        )        
        if not success:
            return False
        
        if wait:
            success = self.wait_no_subscription_odf(my_output=my_output)
            if not success:
                return False

            # or check if pods are not yet there... but normally it takes few seconds for them to disappear
            time.sleep(5)

        return True

    def is_subscription_odf_operator_ready(self):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'ceph-csi-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'csi-addons-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'noobaa-operator'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-console'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'ocs-operator'},
            {'namespace': 'openshift-storage', 'name': 'odf-console'},
            {'namespace': 'openshift-storage', 'name': 'odf-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'prometheus-operator'},
            {'namespace': 'openshift-storage', 'name': 'rook-ceph-operator'},
            {'namespace': 'openshift-storage', 'name': 'ux-backend-server'}
        ]

        for deployment in deployments:
            if not self.is_deployment_ready(deployment['namespace'], deployment['name']):
                return False

        return True
    
    def wait_subscription_odf_ready(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'ceph-csi-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'csi-addons-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'noobaa-operator'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-console'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'ocs-operator'},
            {'namespace': 'openshift-storage', 'name': 'odf-console'},
            {'namespace': 'openshift-storage', 'name': 'odf-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'prometheus-operator'},
            {'namespace': 'openshift-storage', 'name': 'rook-ceph-operator'},
            {'namespace': 'openshift-storage', 'name': 'ux-backend-server'}
        ]
        success = self.wait_deployments_ready_state(deployments, my_output=my_output, optional=False, allow_zero_replicas=True)
        if not success:
            return False

        return True

    def wait_no_subscription_odf(self, my_output=None):
        deployments = [
            {'namespace': 'openshift-storage', 'name': 'ceph-csi-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'csi-addons-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'noobaa-operator'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-console'},
            {'namespace': 'openshift-storage', 'name': 'ocs-client-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'ocs-operator'},
            {'namespace': 'openshift-storage', 'name': 'odf-console'},
            {'namespace': 'openshift-storage', 'name': 'odf-operator-controller-manager'},
            {'namespace': 'openshift-storage', 'name': 'prometheus-operator'},
            {'namespace': 'openshift-storage', 'name': 'rook-ceph-operator'},
            {'namespace': 'openshift-storage', 'name': 'ux-backend-server'}
        ]
        success = self.wait_no_deployments(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        return True
