import yaml
from menu.common import get_confirmation


class K8sClusterVersionDisable():
    def __init__(self):
        pass

    def get_disable_network_operator_management_body(self):
        body = {}
        body['api'] = 'config.openshift.io/v1'
        body['kind'] = 'ClusterVersion'
        body['metadata'] = dict(name='version')
        body['spec'] = {}
        value_mo = {}
        value_mo['kind'] = 'Deployment'
        value_mo['group'] = 'apps'
        value_mo['name'] = 'network-operator'
        value_mo['namespace'] = 'openshift-network-operator'
        value_mo['unmanaged'] = True
        body['spec']['overrides'] = [value_mo]
        return body

    def disable_network_operator_management(
            self, 
            confirmation=False, 
            my_output=None
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Disable network operator management', before_newline=True, underline=True)
            
        cluster_version_mo = self.get_cluster_version(return_mo=True)
        if cluster_version_mo is None:
            if my_output is not None:
                my_output.error('Failed to get cluster version via rest api')
            return False
            
        body = self.get_disable_network_operator_management_body()
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