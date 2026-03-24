from lib import filter_helper
from lib import ip_helper


class K8sUserDefinedNetworkL3():
    def __init__(self):
        pass

    def validate_user_defined_network_l3_subnets(self, subnets):
        v4_subnets = []
        v6_subnets = []

        for subnet in subnets:
            if not isinstance(subnet, dict):
                return False, 'subnet dict required'
            
            cidr = filter_helper.get(subnet, 'cidr')
            if cidr is None:
                return False, 'subnet dict with cidr property required'
            
            host = filter_helper.get(subnet, 'host')
            if host is None:
                return False, 'subnet dict with host property required'

            if not isinstance(host, int):
                return False, 'subnet dict with host int property required'
            
            if ip_helper.is_valid_ipv4_cidr(cidr):
                v4_subnets.append(cidr)
                if int(cidr.split('/')[1]) >= host:
                    return False, 'host length must be greater than cidr length'

                if host > 30:
                    return False, 'invalid v4 host length'
                
                continue

            if ip_helper.is_valid_ipv6_cidr(cidr):
                v6_subnets.append(cidr)
                if int(cidr.split('/')[1]) >= host:
                    return False, 'host length must be greater than cidr length'

                if host != 64:
                    return False, 'invalid v6 host length'

                continue

            return False, 'invalid subnet: %s' % (subnet)

        if len(v4_subnets) > 1:
            return False, 'only one v4 cidr can be defined'
        
        if len(v6_subnets) > 1:
            return False, 'only one v6 cidr can be defined'
        
        for subnet in v6_subnets:
            if subnet.split('/')[1] != '64':
                return False, '/64 v6 cidr required'
        
        if len(v4_subnets) == 0 and len(v6_subnets) == 0:
            return False, 'subnets required'
        
        return True, None
    
    def get_user_defined_network_l3_body(
            self, 
            namespace,
            name,
            primary,
            subnets
        ):
        body = {}
        body['apiVersion'] = 'k8s.ovn.org/v1'
        body['kind'] = 'UserDefinedNetwork'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['topology'] = 'Layer3'
        body['spec']['layer3'] = {}
        if primary:
            body['spec']['layer3']['role'] = 'Primary'
        else:
            body['spec']['layer3']['role'] = 'Secondary'

        body['spec']['layer3']['subnets'] = []
        for item in subnets:
            body['spec']['layer3']['subnets'].append(
                dict(cidr=item['cidr'], hostSubnet=item['host'])
            )

        return body

    def create_user_defined_network_l3(
            self, 
            namespace,
            name,
            primary,
            subnets,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_user_defined_network_l3_body(
            namespace,
            name,
            primary, 
            subnets
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
