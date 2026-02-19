class K8sClusterwidePrivateNetworkDelete():
    def __init__(self):
        pass

    def delete_clusterwide_private_network_webhook(self, my_output=None, wait=True):
        self.delete_mutating_webhook(self.pnet_webhook_name, my_output=my_output, wait=wait)
        
    def delete_clusterwide_private_network(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Clusterwide Private Network', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        network = self.get_clusterwide_private_network(name, pod_info=True, cache_enabled=False)
        if network is None:
            if my_output is not None:
                my_output.default('- already gone')
            return True

        if len(network['pod']) > 0:
            if my_output is not None:
                my_output.error('Pods connected to network')
            return False
        
        if not self.delete_clusterwide_private_network_mo(name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Network deleted', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for not network...')

            if not self.wait_no_clusterwide_private_network(name):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    

    def delete_clusterwide_private_networks(self, my_output=None, wait=True):
        networks = self.get_clusterwide_private_networks(cache_enabled=False)
        if networks is None:
            return True
        
        if len(networks) == 0:
            if my_output is not None:
                my_output.default('No ClusterwidePrivateNetwork crds found')
            return True
        
        for network in networks:
            if not self.delete_clusterwide_private_network(network['name'], wait=wait, my_output=my_output):
                return False
            
        return True
