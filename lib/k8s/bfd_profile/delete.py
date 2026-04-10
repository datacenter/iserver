class K8sBfdProfileDelete():
    def __init__(self):
        pass

    def delete_bfd_profile(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'BFDProfile', 
            'metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='bfd_profile',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_bfd_profile(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def delete_bfd_profiles(self, my_output=None, wait=True):
        peers = self.get_bfd_profiles(
            cache_enabled=False
        )
        if peers is None:
            if my_output is not None:
                my_output.error('Failed to get bgp peers')
            return False

        if len(peers) == 0:
            if my_output is not None:
                my_output.default('Metallb bgp peers %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for peer in peers:
            success = self.delete_bfd_profile(
                peer['namespace'],
                peer['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone