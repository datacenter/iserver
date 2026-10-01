class K8sDeploymentConfigApi():
    def __init__(self):
        self.deployment_config_mo = None

    def get_deployment_config_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.deployment_config_mo
        )
        if cache_hit:
            return response

        response, self.deployment_config_mo = self.get_resources(
            'DeploymentConfig', 
            'apps.openshift.io/v1', 
            self.deployment_config_mo,
            name=name
        )

        return response