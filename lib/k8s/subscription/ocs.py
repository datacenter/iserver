class K8sSubscriptionOcs():
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
