class K8sNodeFeatureDiscoveryCreate():
    def __init__(self):
        pass

    def create_node_feature_discovery(self, body, my_output=None, confirmation=False, wait=True):
        if not self.create_resource(body, object_name='node_feature_discovery', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_node_feature_discovery(
            body['metadata']['namespace'],
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_subscription_nfd_ready(my_output=my_output, with_instance=True)
        if not success:
            return False

        success = self.wait_nodes_annotations(
            ['nfd.node.kubernetes.io/feature-labels'],
            my_output=my_output,
            worker_only=True
        )
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        return True    