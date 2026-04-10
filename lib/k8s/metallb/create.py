class K8sMetalLbCreate():
    def __init__(self):
        pass

    def get_metallb_body(self):
        body = {}
        body['apiVersion'] = 'metallb.io/v1beta1'
        body['kind'] = 'MetalLB'
        body['metadata'] = dict(
            namespace='metallb-system',
            name='metallb'
        )
        return body

    def create_metallb(self, body, my_output=None, confirmation=False, wait=True):
        if body is None:
            body = self.get_metallb_body()

        if not self.create_resource(body, object_name='metallb', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_metallb(
            body['metadata']['namespace'],
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_subscription_metallb_instance_ready(my_output=my_output)
        if not success:
            return False

        return True    