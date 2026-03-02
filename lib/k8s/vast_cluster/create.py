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
        if not self.create_resource(body, object_name='vast_cluster', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_vast_cluster(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
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
