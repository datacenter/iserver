class K8sVastClusterCreate():
    def __init__(self):
        pass

    def get_vast_cluster_body(
            self, 
            namespace,
            name,
            endpoint, 
            username,
            password,
            extras={}
        ):
        body = {}
        body['apiVersion'] = 'storage.vastdata.com/v1'
        body['kind'] = 'VastCluster'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['endpoint'] = endpoint
        body['spec']['username'] = username
        body['spec']['password'] = password

        for key in extras:
            body['spec'][key] = extras[key]

        return body

    def create_vast_cluster(
            self, 
            namespace,
            name,
            endpoint, 
            username,
            password,
            extras={},
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_vast_cluster_body(
            namespace,
            name,
            endpoint, 
            username,
            password,
            extras=extras
        )
        return self.create_vast_cluster_from_body(
            body,
            confirmation=confirmation, 
            my_output=my_output, 
            wait=wait
        )

    def create_vast_cluster_from_body(
        self, 
        body,
        confirmation=False, 
        my_output=None, 
        wait=True
    ):
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        success = self.create_resource_and_wait(
            body, 
            'vast_cluster', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False
        
        if not wait:
            return True
                                    
        success = self.wait_vast_cluster(
            namespace,
            name,
            match_properties={'initialized_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
                            
        success = self.wait_vast_cluster(
            namespace,
            name,
            match_properties={'deployed_status':'True'},
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False

        return True