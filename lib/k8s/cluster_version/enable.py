import yaml
from menu.common import get_confirmation


class K8sClusterVersionEnable():
    def __init__(self):
        pass

    def get_enable_network_operator_management_body(self):
        body = {}
        body['api'] = 'config.openshift.io/v1'
        body['kind'] = 'ClusterVersion'
        body['metadata'] = dict(name='version')
        body['spec'] = {}
        body['spec']['overrides'] = None
        return body

    def enable_network_operator_management(
            self, 
            confirmation=False, 
            my_output=None
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Enable network operator management', before_newline=True, underline=True)
            
        cluster_version_mo = self.get_cluster_version(return_mo=True)
        if cluster_version_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster version via rest api')
            return False
            
        body = self.get_enable_network_operator_management_body()
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        success = self.patch_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        return True    
