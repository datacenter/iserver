from lib import ip_helper


class K8sUserDefinedNetworkL2():
    def __init__(self):
        pass

    def validate_user_defined_network_l2_subnets(self, subnets):
        v4_subnets = []
        v6_subnets = []

        for subnet in subnets:
            if ip_helper.is_valid_ipv4_cidr(subnet):
                v4_subnets.append(subnet)
                continue

            if ip_helper.is_valid_ipv6_cidr(subnet):
                v6_subnets.append(subnet)
                continue

            return False, 'invalid subnet: %s' % (subnet)

        if len(v4_subnets) > 1:
            return False, 'only one v4 cidr can be defined'
        
        if len(v6_subnets) > 1:
            return False, 'only one v6 cidr can be defined'
        
        for subnet in v6_subnets:
            if subnet.split('/')[1] != '64':
                return False, '/64 v6 cidr required'
        
        return True, None
    
    def get_user_defined_network_l2_body(
            self, 
            namespace,
            name,
            primary,
            subnets=[]
        ):
        body = {}
        body['apiVersion'] = 'k8s.ovn.org/v1'
        body['kind'] = 'UserDefinedNetwork'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['topology'] = 'Layer2'
        body['spec']['layer2'] = {}
        if primary:
            body['spec']['layer2']['role'] = 'Primary'
        else:
            body['spec']['layer2']['role'] = 'Secondary'

        if len(subnets) > 0:
            body['spec']['layer2']['subnets'] = subnets
        else:
            body['spec']['ipam'] = dict(mode='Disabled')

        return body

    def create_user_defined_network_l2(
            self, 
            namespace,
            name,
            primary,
            subnets=[],
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_user_defined_network_l2_body(
            namespace,
            name,
            primary, 
            subnets=subnets
        )
        if not self.create_resource(body, object_name='user_defined_network', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_user_defined_network(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_user_defined_network(
            namespace,
            name,
            match_properties={'created_status':'True'},
            break_properties={'created_status':'False'},
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_user_defined_network(
            namespace,
            name,
            match_properties={'allocated_status':'True'},
            break_properties={'allocated_status':'False'},
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return success
