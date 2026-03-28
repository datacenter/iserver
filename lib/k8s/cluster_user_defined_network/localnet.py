from lib import ip_helper


class K8sClusterUserDefinedNetworkLocalnet():
    def __init__(self):
        pass

    def validate_cluster_user_defined_network_localnet_subnets(self, subnets):
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
    
    def get_cluster_user_defined_network_localnet_body(
            self, 
            name,
            namespace,
            phy,
            subnets=[]
        ):
        body = {}
        body['apiVersion'] = 'k8s.ovn.org/v1'
        body['kind'] = 'ClusterUserDefinedNetwork'
        body['metadata'] = {}
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['namespaceSelector'] = {}
        body['spec']['namespaceSelector']['matchExpressions'] = []

        match_mo = {}
        match_mo['key'] = 'kubernetes.io/metadata.name'
        match_mo['operator'] = 'In'
        match_mo['values'] = []
        for item in namespace:
            match_mo['values'].append(item['name'])
        
        body['spec']['namespaceSelector']['matchExpressions'].append(
            match_mo
        )

        body['spec']['network'] = {}
        body['spec']['network']['topology'] = 'Localnet'
        body['spec']['network']['localnet'] = {}
        body['spec']['network']['localnet']['role'] = 'Secondary'
        body['spec']['network']['localnet']['physicalNetworkName'] = phy

        if len(subnets) > 0:
            body['spec']['network']['localnet']['subnets'] = subnets
        else:
            body['spec']['network']['localnet']['ipam'] = dict(mode='Disabled')

        return body

    def create_cluster_user_defined_network_localnet(
            self, 
            name,
            namespace,
            phy,
            subnets=[],
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_cluster_user_defined_network_localnet_body(
            name,
            namespace,
            phy, 
            subnets=subnets
        )
        if not self.create_resource(body, object_name='cluster_user_defined_network', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_cluster_user_defined_network(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        success = self.wait_cluster_user_defined_network(
            name,
            match_properties={'created_status':'True'},
            break_properties={'created_status':'False'},
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return success
