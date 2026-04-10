class K8sBgpAdvertisementDelete():
    def __init__(self):
        pass

    def delete_bgp_advertisement(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'BGPAdvertisement', 
            'metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='bgp_advertisement',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_bgp_advertisement(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def delete_bgp_advertisements(self, my_output=None, wait=True):
        advertisements = self.get_bgp_advertisements(
            cache_enabled=False
        )
        if advertisements is None:
            if my_output is not None:
                my_output.error('Failed to get bgp advertisements')
            return False

        if len(advertisements) == 0:
            if my_output is not None:
                my_output.default('Metallb bgp advertisements %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for advertisement in advertisements:
            success = self.delete_bgp_advertisement(
                advertisement['namespace'],
                advertisement['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone