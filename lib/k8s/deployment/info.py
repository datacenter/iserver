class K8sDeploymentInfo():
    def __init__(self):
        self.deployment = None

    def get_deployment_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )

        keys = [
            'observedGeneration',
            'replicas',
            'updatedReplicas',
            'readyReplicas',
            'availableReplicas',
            'conditions'
        ]
        for key in keys:
            info[key] = self.get(managed_object, 'status:%s' % (key))

        info['spec_replicas'] = self.get(managed_object, 'spec:replicas')

        if info['spec_replicas'] == 0:
            info['readyT'] = '0/0'
            info['__Output']['readyT'] = 'Yellow'
            info['ready'] = True
            return info

        info['ready'] = False
        if info['replicas'] is not None and info['readyReplicas'] is not None:
            if info['replicas'] > 0 and info['replicas'] == info['readyReplicas']:
                info['ready'] = True

        info['readyT'] = '%s/%s' % (
            info['replicas'],
            info['readyReplicas']
        )

        if info['ready']:
            info['readyTick'] = '\u2713'
            info['__Output']['readyT'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['readyTick'] = '\u2717'
            info['__Output']['readyT'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_deployments(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'deployment', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_deployment(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'deployment', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def get_deployment_optimized(self, namespace, name, return_mo=False, cache_enabled=True):
        managed_object = self.get_deployment_mo(
            namespace=namespace, 
            name=name, 
            cache_enabled=cache_enabled
        )
        if return_mo:
            return managed_object
        
        if managed_object is None:
            return None
        
        return self.get_deployment_info(managed_object)

    def is_deployment(self, namespace, name, cache_enabled=True, optimized=False):
        if optimized:
            info = self.get_deployment_optimized(namespace, name, cache_enabled=cache_enabled)
        else:
            info = self.get_deployment(namespace, name, cache_enabled=cache_enabled)

        if info is None:
            return False
        
        return True

    def is_deployment_ready(self, namespace, name, cache_enabled=True, optimized=False):
        if optimized:
            info = self.get_deployment_optimized(namespace, name, cache_enabled=cache_enabled)
        else:
            info = self.get_deployment(namespace, name, cache_enabled=cache_enabled)

        if info is None:
            return False
        
        return info['ready']

    def get_deployment_resources(self, namespace, name, cache_enabled=True):
        resources = {}
        resources['rs'] = []
        resources['pod'] = []

        info = self.get_deployment_optimized(namespace, name, cache_enabled=cache_enabled)
        if info is None:
            return resources

        replica_sets = self.get_replica_set_deployments(namespace, name, cache_enabled=cache_enabled)
        if replica_sets is None:
            return resources
        
        for replica_set in replica_sets:
            resources['rs'].append(
                dict(
                    namespace=replica_set['namespace'],
                    name=replica_set['name']
                )
            )
            pods = self.get_pods_replica_set(namespace, replica_set['name'], cache_enabled=cache_enabled)
            if pods is None:
                continue

            for pod in pods:
                resources['pod'].append(
                    dict(
                        namespace=pod['namespace'],
                        name=pod['name']
                    )
                )

        return resources
