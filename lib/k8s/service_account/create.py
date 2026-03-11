class K8sServiceAccountCreate():
    def __init__(self):
        pass

    def get_service_account_body(
            self, 
            namespace,
            name
        ):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'ServiceAccount'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        return body

    def create_service_account(
            self, 
            namespace,
            name,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_service_account_body(
            namespace,
            name
        )
        if not self.create_resource(body, object_name='service_account', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_service_account(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
