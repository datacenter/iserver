class K8sNodeFeatureDiscoveryDelete():
    def __init__(self):
        pass

    def delete_node_feature_discovery(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'NodeFeatureDiscovery', 
            'nfd.openshift.io/v1',
            name, 
            namespace=namespace, 
            object_name='node_feature_discovery',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_node_feature_discovery(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
    
    def delete_node_feature_discoveries(self, my_output=None, wait=True):
        nfds = self.get_node_feature_discoverys(
            cache_enabled=False
        )
        if nfds is None:
            if my_output is not None:
                my_output.error('Failed to get nfd instances')
            return False

        if len(nfds) == 0:
            if my_output is not None:
                my_output.default('Node feature discovery instances %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for nfd in nfds:
            success = self.delete_node_feature_discovery(
                nfd['namespace'],
                nfd['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone