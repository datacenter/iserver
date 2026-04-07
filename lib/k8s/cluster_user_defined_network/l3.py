from lib import filter_helper
from lib import ip_helper


class K8sClusterUserDefinedNetworkL3():
    def __init__(self):
        pass

    def validate_cluster_user_defined_network_l3_subnets(self, subnets):
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
    
    def get_cluster_user_defined_network_l3_body(
            self, 
            name,
            namespace,
            primary,
            subnets,
            labels={}
        ):
        body = {}
        body['apiVersion'] = 'k8s.ovn.org/v1'
        body['kind'] = 'ClusterUserDefinedNetwork'
        body['metadata'] = {}
        body['metadata']['name'] = name
        if len(labels) > 0:
            body['metadata']['labels'] = {}
            for label in labels:
                body['metadata']['labels'][label] = labels[label]

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
        body['spec']['network']['topology'] = 'Layer3'

        body['spec']['network']['layer3'] = {}
        if primary:
            body['spec']['network']['layer3']['role'] = 'Primary'
        else:
            body['spec']['network']['layer3']['role'] = 'Secondary'

        body['spec']['network']['layer3']['subnets'] = []
        for item in subnets:
            body['spec']['network']['layer3']['subnets'].append(
                dict(cidr=item['cidr'], hostSubnet=item['host'])
            )

        return body

    def create_cluster_user_defined_network_l3(
            self, 
            name,
            namespace,
            primary,
            subnets,
            labels={},
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_cluster_user_defined_network_l3_body(
            name,
            namespace,
            primary, 
            subnets,
            labels=labels
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

        for item in namespace:
            success = self.wait_nad(
                item['name'],
                name,
                max_time=60,
                my_output=my_output
            )
            if not success:
                return False            

        return success
