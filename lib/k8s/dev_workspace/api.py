class K8sDevWorkspaceApi():
    def __init__(self):
        self.dev_workspace_mo = None
        self.dev_workspace_namespace_mo = {}

    def get_dev_workspace_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.dev_workspace_mo,
            self.dev_workspace_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.dev_workspace_mo, self.dev_workspace_namespace_mo = self.get_namespaced_resources(
            'DevWorkspace', 
            'workspace.devfile.io/v1alpha2', 
            self.dev_workspace_mo,
            self.dev_workspace_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_dev_workspace_mo(self, namespace, name):
        success, _ = self.delete_resource('DevWorkspace', 'workspace.devfile.io/v1alpha2', name, namespace=namespace)
        return success