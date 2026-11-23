class K8sNetworkOperatorUpdate():
    def __init__(self):
        pass
    
    def get_cluster_network_operator_body(self, network_operator_type, cidr, host_prefix, kube_proxy_replacement=False):
        body = {}
        body['apiVersion'] = 'operator.openshift.io/v1'
        body['kind'] = 'Network'
        body['metadata'] = dict(name='cluster')
        body['spec'] = {}
        body['spec']['defaultNetowkr'] = dict(type=network_operator_type)
        network_mo = {}
        network_mo['cidr'] = cidr
        network_mo['hostPrefix'] = host_prefix
        body['spec']['clusterNetwork'] = [network_mo]
        body['spec']['deployKubeProxy'] = kube_proxy_replacement
        body['status'] = None
        return body

    def set_cluster_network_operator_type(self, network_operator_type, cidr, host_prefix, kube_proxy_replacement=False, confirmation=False, my_output=None, wait=True):
        success = self.patch_resource(
            self.get_cluster_network_operator_body(
                network_operator_type, 
                cidr, 
                host_prefix, 
                kube_proxy_replacement=kube_proxy_replacement
            ), 
            object_name='network_operator', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        return True

    def enable_ovn_frr(self, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if not self.is_cluster_network_operator_ovn(cache_enabled=False):
            if my_output is not None:
                my_output.error('OVNKubnernetes CNI required')
            return False
        
        if self.is_ovn_frr_enabled(cache_enabled=True):
            if my_output is not None:
                my_output.default('ovn k8s-frr %s' % (my_output.add_color('already enabled', 'Green')))
            return True

        if self.is_cluster_network_operator_progressing(cache_enabled=True):
            if my_output is not None:
                my_output.default('Cluster operator is %s' % (my_output.add_color('progressing', 'Red')))
            return False
        
        # "spec": {
        #     "additionalRoutingCapabilities": {
        #       "providers": ["FRR"]
        #     }
        # }

        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True),
            exclude=['resourceVersion']
        )
        managed_object['spec']['additionalRoutingCapabilities'] = dict(providers=['FRR'])
    
        success = self.patch_resource(
            managed_object,
            object_name='network_operator', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'True'},
            max_time=120,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'False'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def disable_ovn_frr(self, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if not self.is_cluster_network_operator_ovn(cache_enabled=False):
            if my_output is not None:
                my_output.error('OVNKubnernetes CNI required')
            return False
        
        if not self.is_ovn_frr_enabled(cache_enabled=True):
            if my_output is not None:
                my_output.default('ovn k8s-frr %s' % (my_output.add_color('already disabled', 'Green')))
            return True

        if self.is_cluster_network_operator_progressing(cache_enabled=True):
            if my_output is not None:
                my_output.default('Cluster operator is %s' % (my_output.add_color('progressing', 'Red')))
            return False
        
        pods = self.get_pods(namespace='openshift-frr-k8s', cache_enabled=False)
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to get pods in openshift-frr-k8s namespace')
            return False
        
        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True, cache_enabled=False),
            exclude=['resourceVersion']
        )
        del managed_object['spec']['additionalRoutingCapabilities']
    
        success = self.replace_resource(
            managed_object,
            object_name='network_operator', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_no_pods(
            pods, 
            max_time=120, 
            prompt='Pod', 
            my_output=my_output
        )

        return success
    
    def enable_ovn_frr_ra(self, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if not self.is_cluster_network_operator_ovn(cache_enabled=False):
            if my_output is not None:
                my_output.error('OVNKubnernetes CNI required')
            return False
        
        if self.is_ovn_frr_ra_enabled(cache_enabled=True):
            if my_output is not None:
                my_output.default('ovn k8s-frr route advertisement %s' % (my_output.add_color('already enabled', 'Green')))
            return True

        if self.is_cluster_network_operator_progressing(cache_enabled=True):
            if my_output is not None:
                my_output.default('Cluster operator is %s' % (my_output.add_color('progressing', 'Red')))
            return False

        pods = self.get_pods(namespace='openshift-ovn-kubernetes', cache_enabled=False)
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to get pods in openshift-frr-k8s namespace')
            return False
        
        # "spec": {
        #     "defaultNetwork": {
        #         "ovnKubernetesConfig": {
        #             "routeAdvertisements": "Enabled"
        #         }
        #     }
        # }

        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True),
            exclude=['resourceVersion']
        )
        managed_object['spec']['defaultNetwork'] = dict(ovnKubernetesConfig=dict(routeAdvertisements='Enabled'))
    
        success = self.patch_resource(
            managed_object,
            object_name='network_operator', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'True'},
            max_time=120,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'False'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_no_pods(
            pods, 
            max_time=120, 
            prompt='Pod', 
            my_output=my_output
        )
        if not success:
            return False
        
        success = self.wait_deployment_ready_state(
            'openshift-ovn-kubernetes', 
            'ovnkube-control-plane', 
            max_time=180, 
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_daemon_set_ready_state(
            'openshift-ovn-kubernetes', 
            'ovnkube-node', 
            max_time=180, 
            my_output=my_output
        )
        if not success:
            return False

        return True

    def disable_ovn_frr_ra(self, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if not self.is_cluster_network_operator_ovn(cache_enabled=False):
            if my_output is not None:
                my_output.error('OVNKubnernetes CNI required')
            return False
        
        if not self.is_ovn_frr_ra_enabled(cache_enabled=True):
            if my_output is not None:
                my_output.default('ovn k8s-frr route advertisement %s' % (my_output.add_color('already disabled', 'Green')))
            return True

        if self.is_cluster_network_operator_progressing(cache_enabled=True):
            if my_output is not None:
                my_output.default('Cluster operator is %s' % (my_output.add_color('progressing', 'Red')))
            return False

        pods = self.get_pods(namespace='openshift-ovn-kubernetes', cache_enabled=False)
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to get pods in openshift-frr-k8s namespace')
            return False
        
        # "spec": {
        #     "defaultNetwork": {
        #         "ovnKubernetesConfig": {
        #             "routeAdvertisements": "Enabled"
        #         }
        #     }
        # }

        managed_object = self.cleanup_managed_object(
            self.get_cluster_network_operator(return_mo=True, cache_enabled=False),
            exclude=['resourceVersion']
        )
        del managed_object['spec']['defaultNetwork']['ovnKubernetesConfig']['routeAdvertisements']
    
        success = self.replace_resource(
            managed_object,
            object_name='network_operator', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'True'},
            max_time=120,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_network_operator(
            'cluster',
            match_properties={'Progressing_status':'False'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
        
        success = self.wait_no_pods(
            pods, 
            max_time=120, 
            prompt='Pod', 
            my_output=my_output
        )
        if not success:
            return False
        
        success = self.wait_deployment_ready_state(
            'openshift-ovn-kubernetes', 
            'ovnkube-control-plane', 
            max_time=180, 
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_daemon_set_ready_state(
            'openshift-ovn-kubernetes', 
            'ovnkube-node', 
            max_time=180, 
            my_output=my_output
        )
        if not success:
            return False

        return True
