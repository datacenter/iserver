import yaml
from menu.common import get_confirmation


class K8sClusterwidePrivateNetworkCreate():
    def __init__(self):
        pass

    def get_clusterwide_private_network_body(self, name, subnets, nad=[]):
        body = {}
        body['apiVersion'] = 'isovalent.com/v1alpha1'
        body['kind'] = 'ClusterwidePrivateNetwork'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['subnets'] = subnets

        if len(nad) == 1:
            body['spec']['networkAttachmentDefinitions'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector']['matchLabels'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector']['matchLabels']['kubernetes.io/metadata.name'] = nad[0]

        if len(nad) > 1:
            body['spec']['networkAttachmentDefinitions'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector']['matchExpressions'] = {}
            body['spec']['networkAttachmentDefinitions']['namespaceSelector']['matchExpressions'] = []
            
            exporession_mo = {}
            exporession_mo['key'] = 'kubernetes.io/metadata.name'
            exporession_mo['operator'] = 'In'
            exporession_mo['values'] = nad
            body['spec']['networkAttachmentDefinitions']['namespaceSelector']['matchExpressions'].append(exporession_mo)

        return body
    
    def create_clusterwide_private_network(self, name, subnet, nad=[], confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Clusterwide Private Network', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if self.is_clusterwide_private_network(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        body = self.get_clusterwide_private_network_body(
            name,
            subnet,
            nad=nad
        )
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        success, _ = self.create_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Network created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for network...')

            if not self.wait_clusterwide_private_network(name):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True