class K8sIpAddressPoolCreate():
    def __init__(self):
        pass

    def get_ip_address_pool_body(self, namespace, name, addr):
        body = {}
        body['apiVersion'] = 'metallb.io/v1beta1'
        body['kind'] = 'IPAddressPool'
        body['metadata'] = dict(
           namespace=namespace,
           name=name
        )
        body['spec'] = {}
        body['spec']['addresses'] = addr
        return body
    
    def create_ip_address_pool(self, namespace, name, addr, my_output=None, confirmation=False, wait=True):
        success = self.create_resource(
            self.get_ip_address_pool_body(
                namespace,
                name,
                addr
            ), 
            object_name='ip_address_pool', 
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_ip_address_pool(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True    