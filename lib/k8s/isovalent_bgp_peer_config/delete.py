class K8sIsovalentBGPPeerConfigDelete():
    def __init__(self):
        pass
    
    def delete_isovalent_bgp_peer_config(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete BGP Peer Config', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_isovalent_bgp_peer_config(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        success = self.delete_isovalent_bgp_peer_config_mo(name)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('- wait for no crd')

        success = self.wait_no_isovalent_bgp_peer_config(name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            return False
        
        return True

    def delete_isovalent_bgp_peer_configs(self, my_output=None, wait=True, brief=False):
        managed_objects = self.get_isovalent_bgp_peer_config_mo(cache_enabled=False)
        if managed_objects is None:
            if my_output is not None:
                my_output.error('Failed to get IsovalentBGPPeerConfig CRDs')
            return False
        
        if len(managed_objects) == 0 and my_output is not None:
            if my_output is not None:
                my_output.default('All IsovalentBGPPeerConfig CRDs %s' % (my_output.add_color('already deleted', 'Green')))

        for managed_object in managed_objects:
            if brief:
                success = self.delete_isovalent_bgp_peer_config(
                    managed_object['metadata']['name'],
                    my_output=None, 
                    wait=wait
                )
            else:
                success = self.delete_isovalent_bgp_peer_config(
                    managed_object['metadata']['name'],
                    my_output=my_output, 
                    wait=wait
                )

            if success:
                if my_output is not None:
                    my_output.default('IsovalentBGPPeerConfig %s %s' % (managed_object['metadata']['name'], my_output.add_color('deleted', 'Green')))
            else:
                if my_output is not None:
                    my_output.default('IsovalentBGPPeerConfig %s %s' % (managed_object['metadata']['name'], my_output.add_color('delete failed', 'Red')))
                return False
            
        return True
